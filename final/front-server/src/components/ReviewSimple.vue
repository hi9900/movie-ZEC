<template>
  <v-container>
    <!-- 내가 가진 리뷰 데이터가 있으면 색칠 하기 -->
    <v-card class="actions-panel__card d-none d-md-block" tile>
      <v-card-text class="py-0 px-0">
        <v-row>
          <v-col cols="6" class="text-center" py-2>
            <v-icon :color="WatchIconColor" class="mx-2">mdi-eye</v-icon>
          </v-col>
          <v-col cols="6" class="text-center" py-2>
            <v-icon :color="heartIconColor" class="mx-2">mdi-heart</v-icon>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6" class="text-center" py-2>
            <v-btn icon @click="showReviewModal = true" class="mx-2"
              ><v-icon>mdi-pencil</v-icon></v-btn
            >
          </v-col>
          <v-col cols="6" class="text-center" py-2>
            <v-btn icon @click="sharePage" class="mx-2">
              <v-icon>mdi-share-variant</v-icon>
            </v-btn>
          </v-col>
        </v-row>
      </v-card-text>
    </v-card>

    <!-- 리뷰 작성 모달 -->
    <v-dialog v-model="showReviewModal" max-width="600px">
      <v-card>
        <v-card-title class="text-h5"> 리뷰 작성하기 </v-card-title>
        <v-card-text>
          <v-row>
            <v-col cols="3">
              <v-img
                :src="`https://www.themoviedb.org/t/p/original/${movie.poster_path}`"
                alt="영화 포스터"
                height="150px"
                width="100px"
              />
            </v-col>
            <v-col cols="9">
              <h3>{{ movie.title }}</h3>

              <v-row>
                <v-col>
                  <v-btn icon @click="toggleWatch">
                    <v-icon :color="watched || isWatched ? 'primary' : 'grey'"
                      >mdi-eye</v-icon
                    ></v-btn
                  >
                  <v-btn icon @click="toggleHeart">
                    <v-icon :color="heartIconColor">mdi-heart</v-icon></v-btn
                  >
                </v-col>
              </v-row>

              <v-row class="mt-5">
                <v-col class="d-flex align-items-center">
                  <v-rating
                    v-model="rating"
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
            v-model="reviewText"
            placeholder="영화에 대한 의견을 작성해주세요."
            rows="5"
            outlined
          ></v-textarea>
          <!-- 태그 작성란 -->
          <!-- <v-row class="my-4">
             <v-chip-group
                      column
                      v-model="tagSelection"
                      multiple
                      :mandatory="false">
                  <v-chip
                          v-for="tag in tags"
                          :key="tag"
                  >
                      {{ tag }}
          </v-chip>
          </v-chip-group>
          </v-row> -->
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" @click.prevent="submitReview"> 작성 </v-btn>
          <v-btn text color="grey" @click="showReviewModal = false">
            취소
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  data() {
    return {
      liked: false,
      hearted: false,
      watched: false,
      rating: 0,
      showReviewModal: false,
      reviewText: ''
      // 날짜 받아서 적기
      // watched_at: null
    }
  },
  props: {
    movie: [Object, Array]
  },
  methods: {
    toggleLike() {
      this.liked = !this.liked
    },
    toggleHeart() {
      this.hearted = !this.hearted
    },
    toggleWatch() {
      this.watched = !this.watched
    },

    updateWatchedStatus() {
      this.watched = this.rating > 0 || this.reviewText !== ''
    },

    // 리뷰 제출
    submitReview() {
      const movieId = this.movie.id
      const Token = this.myToken
      console.log(movieId, Token)
      const data = {
        movie: movieId,
        content: this.reviewText,
        rating: this.rating,
        watched: this.watched,
        // watched_at: this.watched_at,
        like: this.hearted
      }
      axios({
        url: `${API_URL}/api/v1/movies/${movieId}/reviews/`,
        method: 'post',
        headers: {
          Authorization: `Bearer ${Token}`
        },
        data
      })
        .then(res => {
          console.log(res)
          this.showReviewModal = false
          this.reviewText = ''
        })
        .catch(err => console.log(err))
    },
    sharePage() {
      if (navigator.share) {
        navigator.share({
          title: '영화 페이지 공유하기',
          text: '이 영화 페이지를 확인하세요!',
          url: window.location.href
        })
      } else {
        console.log('Web Share API를 지원하지 않는 브라우저입니다.')
      }
    }
  },
  computed: {
    heartIconColor() {
      return this.hearted ? 'red' : 'grey'
    },
    WatchIconColor() {
      return this.watched ? 'blue' : 'grey'
    },
    myToken() {
      return this.$store.state.account.accessToken
    }
  }
}
</script>

<style scoped>
.actions-panel__card {
  max-width: 300px;
  padding: 1rem;
}

.actions-panel__rating {
  flex-direction: column;
  width: 100%;
  align-items: center;
}
</style>
