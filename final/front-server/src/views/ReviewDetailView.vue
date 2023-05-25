<template>
  <v-skeleton-loader v-if="!review"></v-skeleton-loader>
  <v-container v-else>
    <v-row>
      <!-- 영화 정보 -->
      <v-col cols="2">
        <v-row @click="goToDetail" justify="center">
          <v-col class="text-center">
            <v-img
              :src="`https://www.themoviedb.org/t/p/original/${review.movie.poster_path}`"
              alt="영화 포스터"
              width="140px"
              class="mx-auto"
            />
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <h1 class="original-title">{{ review.movie.title }}</h1>
            <p class="text-spacing">{{ review.movie.original_title }}</p>
          </v-col>
        </v-row>
      </v-col>

      <v-col>
        <v-row align="center" justify="center">
          <v-col cols="auto" class="mt-3">
            <router-link
              :to="{name: 'Profile', params: {username: review.user.username}}"
              class="user-profile-link"
            >
              <v-avatar>
                <img
                  :src="`https://source.boringavatars.com/beam/40/${review.user?.username}`"
                  alt="User Avatar"
                />
              </v-avatar>
              <p style="display: flex; justify-content: center">
                {{ review.user.username }}
              </p>
            </router-link>
          </v-col>
          <v-col>
            <p>{{ review.content }}</p>
          </v-col>
        </v-row>

        <v-row justify="space-between" align="center">
          <v-col cols="auto">
            <v-rating
              v-model="review.rating"
              color="yellow"
              background-color="grey"
              size="20"
              :step="0.5"
              :half-increments="true"
              readonly
            ></v-rating>
          </v-col>
          <v-col cols="auto">
            <p>{{ review.watched_at.slice(0, 10) }}</p>
          </v-col>
        </v-row>

        <v-row
          style="
            display: flex;
            align-items: center;
            justify-content: space-between;
          "
        >
          <v-col cols="auto">
            <!-- 리뷰에 대한 좋아요 구현하기 -->
            <!-- <v-btn icon @click.prevent="like">
              <v-icon>mdi-heart</v-icon>
            </v-btn>
            {{ review.like_users.length }} -->
          </v-col>
          <v-col cols="auto">
            <div v-if="review.user.username === username">
              <!-- 수정 버튼을 누르면 수정하는 폼을 띄워서 수정할 수 있게 만들기 -->
              <v-btn @click="editReview()"> 수정 </v-btn>

              <v-btn @click="deleteReview()">삭제</v-btn>
            </div>
          </v-col>
        </v-row>
      </v-col>
    </v-row>

    <!-- 수정 -->

    <v-dialog max-width="600px" v-model="open">
      <v-card>
        <v-card-title class="font-weight-black"> 리뷰 수정하기 </v-card-title>
        <v-card-text>
          <v-row mb-3>
            <v-col cols="3">
              <v-img
                :src="`https://www.themoviedb.org/t/p/original/${review.movie.poster_path}`"
                alt="영화 포스터"
                height="150px"
                width="100px"
              />
            </v-col>

            <v-col cols="9">
              <div class="my-3 font-weight-bold">
                <h2>{{ review.movie.title }}</h2>
                <span>{{ review.movie.original_title }}</span>
              </div>

              <v-row no-gutters class="mb-1">
                <v-col>
                  <v-btn icon @click="toggleWatch">
                    <v-icon color="blue">mdi-eye</v-icon></v-btn
                  >
                  <!-- 날짜 고치는게 고장나서 숨김;; -->
                  <!-- <v-menu
                    ref="menu"
                    v-model="menu"
                    :close-on-content-click="true"
                    transition="scale-transition"
                    offset-y
                    min-width="290px"
                    nudge-right="80"
                  >
                    <template v-slot:activator="{on, attrs}">
                      <v-btn icon v-bind="attrs" v-on="on">
                        <v-icon>mdi-calendar</v-icon>
                      </v-btn>
                    </template>
                    <v-date-picker v-model="this.updateWatched"></v-date-picker>
                  </v-menu>
                  <span class="watched-date ml-2">
                    <strong>{{ this.updateWatched }}</strong>
                  </span> -->
                </v-col>
              </v-row>

              <v-row no-gutters class="mb-1">
                <v-col class="d-flex align-items-center">
                  <v-rating
                    v-model="updateRating"
                    color="yellow"
                    background-color="grey"
                    size="30"
                    :step="0.5"
                    :half-increments="true"
                  />
                  <span class="rating-number ml-2">{{ rating }}</span>
                </v-col>
              </v-row>
            </v-col>
          </v-row>

          <!-- 리뷰 작성란 -->
          <v-textarea
            v-model="updateContent"
            placeholder="영화에 대한 의견을 작성해주세요."
            rows="5"
            outlined
          ></v-textarea>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn elevation="5" color="secondary" @click.prevent="submitReview"
            >수정</v-btn
          >
          <v-btn elevation="5" text @click="open = false">취소</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- 댓글 -->
    <v-row>
      <v-col>
        <h3>댓글 ({{ this.realcomments?.length }})</h3>
        <v-divider></v-divider>
      </v-col>
    </v-row>

    <v-row v-if="this.realcomments">
      <v-col>
        <div
          v-for="comment in this.realcomments"
          :key="comment.id"
          class="py-2"
        >
          <strong class="text-capitalize pr-3">{{
            comment.user.username
          }}</strong>
          <small>{{ comment.created_at.slice(0, 10) }} 작성</small>
          <div
            style="
              display: flex;
              justify-content: space-between;
              align-items: center;
            "
          >
            <div class="pl-3">{{ comment.content }}</div>
            <div v-if="comment.user.username === username" class="pl-3">
              <!-- <v-btn small>수정</v-btn> -->
              <v-btn small @click="deleteComment(comment.id)">삭제</v-btn>
            </div>
          </div>
          <ReplyForm :comment="comment" @createReply="createReply" />
        </div>
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <!-- 댓글 작성 -->
        <!-- <CommentForm @ /> -->
        <v-container>
          <v-row>
            <v-text-field
              v-model="newComment"
              label=""
              @keyup.enter="createComment"
              rows="1"
            />
            <v-btn color="primary" @click.prevent="createComment">작성</v-btn>
          </v-row>
        </v-container>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
import ReplyForm from '@/components/ReplyForm'
// import CommentForm from '@/components/CommentForm'

export default {
  components: {
    ReplyForm
    // CommentForm
  },
  data() {
    return {
      review: null,
      // comments: null,
      newComment: '',
      newreply: '',
      open: false,
      updateRating: null,
      updateContent: null,
      upadateHearted: null,
      updateWatched: null
    }
  },
  methods: {
    // toggleHeart() {
    //   this.upadateHearted = !this.upadateHearted
    // },
    // updateWatchedStatus() {
    //   this.watched = this.rating > 0 || this.reviewText !== ''
    // },
    getReview() {
      const Token = this.myToken
      const reviewId = this.$route.params.reviewId
      // console.log(reviewId)
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/reviews/${reviewId}/`,
        headers: {
          Authorization: `Bearer ${Token}`
        }
      })
        .then(res => {
          console.log(res.data)
          console.log('나는 겟')
          this.review = res?.data
          this.updateRating = res.data?.rating
          this.updateContent = res.data?.content

          // this.upadateHearted = res.data.like
          // this.updateWatched = res.data.watched
        })
        .catch(err => console.log(err))
    },
    // 리뷰 삭제
    deleteReview() {
      const Token = this.myToken
      const reviewId = this.$route.params.reviewId

      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/api/v1/reviews/${reviewId}/`,
        headers: {
          Authorization: `Bearer ${Token}`
        }
      })
        .then(res => {
          console.log(res)
          alert('삭제되었습니다.')
          this.$router.go(-1)
        })
        .catch(e => console.log(e))
    },
    // 리뷰수정
    editReview() {
      // 리뷰 수정 버튼을 클릭할 때마다 다이얼로그를 열고 선택된 리뷰 정보를 저장합니다.
      this.open = true
    },
    // 수정한 리뷰 제출
    submitReview() {
      const Token = this.myToken
      const reviewId = this.$route.params.reviewId
      const data = {
        content: this.updateContent,
        rating: this.updateRating,
        watched: this.updateWatched,
        like: this.upadateHearted
      }
      axios({
        method: 'put',
        url: `http://127.0.0.1:8000/api/v1/reviews/${reviewId}/`,
        headers: {
          Authorization: `Bearer ${Token}`
        },
        data
      }).then(res => {
        console.log(res.data)
        this.open = false
        this.getReview()
      })
      // 리뷰 수정 내용을 저장합니다.
    },

    // 댓글 생성
    // 컴포넌트 나눠서 emit처리를 해야하나?
    createComment() {
      if (this.newComment === '') {
        alert('내용을 입력해주세요.')
      } else {
        const Token = this.myToken
        const reviewId = this.$route.params.reviewId
        const data = {
          // user: this.userId,
          content: this.newComment
        }
        axios({
          method: 'post',
          url: `http://127.0.0.1:8000/api/v1/reviews/${reviewId}/comments/`,
          headers: {
            Authorization: `Bearer ${Token}`
          },
          data
        }).then(() => {
          // console.log(res.data)
          console.log('나는 댓글')
          this.newComment = ''
          this.getReview()
          // this.comments = res.data
        })
      }
    },
    deleteComment(commentId) {
      const Token = this.myToken

      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/api/v1/comments/${commentId}/`,
        headers: {
          Authorization: `Bearer ${Token}`
        }
      })
        .then(res => {
          console.log(res)
          alert('삭제되었습니다.')
          this.getReview()
        })
        .catch(e => console.log(e))
    },
    // 대댓글 작성
    createReply(childData) {
      const Token = this.myToken
      const reviewId = this.$route.params.reviewId
      const commentId = childData.commentId
      const data = {
        content: childData.newreply
      }
      console.log(data)
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/reviews/${reviewId}/comments/${commentId}/replies/`,
        headers: {
          Authorization: `Bearer ${Token}`
        },
        data
      })
        .then(res => {
          console.log('나는 대댓글')
          console.log(res)
          this.getReview()
        })
        .catch(e => console.log(e))
      // event.preventDefault()
    },
    goToDetail() {
      this.$router.push({
        name: 'MovieDetail',
        params: {id: this.review.movie.id}
      })
    }
  },
  created() {
    this.getReview()
    // this.getComment()
  },
  computed: {
    myToken() {
      return this.$store.state.account.accessToken
    },
    comments() {
      return this.review?.comments
    },
    username() {
      return this.$store.state.account.username
    },
    userId() {
      return this.$store.state.account.userId
    },
    realcomments() {
      return this.comments?.filter(comment => comment.parent_comment === null)
    }
  }
}
</script>
<style scoped>
.comment-body {
  margin-bottom: 12px;
}
.text_capitalize {
  text-transform: capitalize;
}
.img-spacing {
  margin-bottom: 16px;
}

.text-spacing {
  margin-right: 16px;
}

.original-title {
  font-size: 20px;
}
.user-profile-link {
  text-decoration: none;
  color: inherit;
}

.user-profile-link:hover {
  cursor: pointer;
  text-decoration: underline;
}
.v-dialog > .v-card > .v-card__text {
  padding: 0 24px 0px;
}
</style>
