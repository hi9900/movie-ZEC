<template>
  <v-skeleton-loader v-if="!review"></v-skeleton-loader>
  <v-container v-else>
    <v-row>
      <v-col>
        <!-- 누르면 영화 상세 페이지로 -->
        <!-- <movie-detail :movie="movie" /> -->
        <v-img
          :src="`https://www.themoviedb.org/t/p/original/${review.movie.poster_path}`"
          alt="영화 포스터"
          height="150px"
          width="100px"
        />

        <p>{{ review.movie.title }}</p>
        <p>{{ review.movie.original_title }}</p>
      </v-col>
      <v-col>
        <p>{{ review.user.username }}</p>
        <p>{{ review.content }}</p>
        <v-rating
          v-model="review.rating"
          color="yellow"
          background-color="grey"
          size="20"
          :step="0.5"
          :half-increments="true"
          readonly
        ></v-rating>
        <v-icon :color="review.like ? 'red' : 'grey'">mdi-heart</v-icon>
        <v-icon :color="review.watched ? 'primary' : 'grey'">mdi-eye</v-icon>
        <p>{{ review.watched_at.slice(0, 10) }}</p>
        <p>
          <!-- 리뷰에 대한 좋아요 구현하기 -->
          <v-btn icon @click="like">
            <v-icon>mdi-heart</v-icon>
          </v-btn>
          {{ review.like_users.length }}
        </p>
        <div v-if="review.user.username === username">
          <!-- 수정 버튼을 누르면 수정하는 폼을 띄워서 수정할 수 있게 만들기 -->
          <v-btn @click="editReview()">수정</v-btn>
          <v-btn @click="deleteReview">삭제</v-btn>
        </div>
      </v-col>
    </v-row>

    <!-- 수정 -->
    <!-- 기존 리뷰내용이랑 바인딩 -->
    <!-- 오류 개많이나는데 되긴 함 -->
    <v-dialog v-model="open">
      <v-card>
        <v-card-title class="text-h5"> 리뷰 수정 </v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="3">
              <v-img
                :src="`https://www.themoviedb.org/t/p/original/${review.movie.poster_path}`"
                alt="영화 포스터"
                height="150px"
                width="100px"
              />
            </v-col>
            <v-col cols="9">
              <h3>{{ review.movie.title }}</h3>

              <v-row>
                <v-col>
                  <v-btn icon @click="toggleWatch">
                    <v-icon
                      :color="review.watched || isWatched ? 'primary' : 'grey'"
                      >mdi-eye</v-icon
                    ></v-btn
                  >
                  <v-btn icon @click="toggleHeart">
                    <v-icon :color="upadateHearted ? 'red' : 'grey'"
                      >mdi-heart</v-icon
                    ></v-btn
                  >
                </v-col>
              </v-row>

              <v-row class="mt-5">
                <v-col class="d-flex align-items-center">
                  <v-rating
                    v-model="updateRating"
                    color="yellow"
                    background-color="grey"
                    size="20"
                    :step="0.5"
                    :half-increments="true"
                    @input="updateWatchedStatus"
                  />
                  <span class="rating-number ml-2">{{ rating }}</span>
                </v-col>
              </v-row>
            </v-col>
          </v-row>

          <!-- 리뷰 작성란 -->
          <v-textarea
            @input="updateWatchedStatus"
            v-model="updateContent"
            rows="5"
            outlined
          ></v-textarea>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="success" @click.prevent="submitReview">수정</v-btn>
          <v-btn @click="open = false">취소</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-row>
      <v-col>
        <h3>댓글 ({{ comments?.length }})</h3>
        <v-divider></v-divider>
      </v-col>
    </v-row>

    <v-row v-if="comments">
      <v-col>
        <div v-for="comment in comments" :key="comment.id" class="py-2">
          <strong class="text-capitalize pr-3">{{
            comment.user.username
          }}</strong>
          <small>{{ comment.created_at.slice(0, 10) }} 작성</small>
          <div class="pl-3">{{ comment.content }}</div>
          <div v-if="comment.user.username === username" class="pl-3">
            <!-- <v-btn small>수정</v-btn> -->
            <v-btn small @click="deleteComment(comment.id)">삭제</v-btn>
          </div>
          <ReplyForm :comment="comment" @createReply="createReply" />
        </div>
      </v-col>
    </v-row>

    <v-row>
      <v-col>
        <!-- 댓글 작성 -->
        <!-- 너무 커 작게 만들기 -->
        <v-card>
          <v-card-text>
            <v-textarea
              v-model="newComment"
              label="Your comment"
              @keyup.enter="createComment"
              rows="1"
            />
          </v-card-text>
          <v-card-actions>
            <v-btn color="primary" @click.prevent="createComment"
              >댓글 작성</v-btn
            >
          </v-card-actions>
        </v-card>
        <!-- 로그인 시 작성할 수 있게 -->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
import ReplyForm from '@/components/ReplyForm'

export default {
  components: {
    ReplyForm
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
    toggleHeart() {
      this.upadateHearted = !this.upadateHearted
    },
    updateWatchedStatus() {
      this.watched = this.rating > 0 || this.reviewText !== ''
    },
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
          this.review = res.data
          this.updateRating = res.data.rating
          this.updateContent = res.data.content
          this.upadateHearted = res.data.like
          this.updateWatched = res.data.watched
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

    submitReview() {
      const Token = this.myToken
      const reviewId = this.$route.params.reviewId
      const data = {
        content: this.updateContent,
        rating: this.updateRating,
        watched: this.updateWatched,
        // watched_at: this.watched_at,
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

    // 댓글 가져오기
    // getComment() {
    //   const Token = this.myToken
    //   const reviewId = this.$route.params.reviewId
    //   axios({
    //     method: 'get',
    //     url: `http://127.0.0.1:8000/api/v1/reviews/${reviewId}/comments/`,
    //     headers: {
    //       Authorization: `Bearer ${Token}`
    //     },
    //   })
    //   .then((res) => {
    //     console.log(res.data)
    //     // push 말고 맨 앞에 가져오거나 뭐 어케해야함
    //     this.comments = res.data
    //   })
    // },
    // 댓글 생성
    // 컴포넌트 나눠서 emit처리를 해야하나?
    createComment() {
      if (this.newComment === '') {
        // alert말고 뭐 어케든 하기
        alert('입력해')
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
      axios({
        method: 'post',
        url: `http://127.0.0.1:8000/api/v1/reviews/${reviewId}/comments/${commentId}/replies/`,
        headers: {
          Authorization: `Bearer ${Token}`
        },
        data
      })
        .then(res => {
          console.log(res)
          this.getReview()
        })
        .catch(e => console.log(e))
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
      return this.review.comments
    },
    username() {
      return this.$store.state.account.username
    },
    userId() {
      return this.$store.state.account.userId
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
</style>
