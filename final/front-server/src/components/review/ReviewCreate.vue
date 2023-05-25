<!-- src/components/ReviewForm.vue -->
<template>
  <v-card>
    <v-card-title class="font-weight-black"> 리뷰 작성하기 </v-card-title>
    <v-card-text>
      <v-row mb-3>
        <v-col cols="3">
          <v-img
            :src="`https://www.themoviedb.org/t/p/original/${movie?.poster_path}`"
            alt="영화 포스터"
            height="150px"
            width="100px"
          />
        </v-col>

        <v-col cols="9">
          <div class="my-3 font-weight-bold">
            <h2>{{ movie.title }}</h2>
            <span>{{ movie.original_title }}</span>
          </div>
          <v-row no-gutters class="mb-1">
            <v-col>
              <v-btn icon> <v-icon color="blue">mdi-eye</v-icon></v-btn>
              <!-- 옆에 날짜 추가 -->
              <v-menu
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
                <v-date-picker v-model="watched_date"></v-date-picker>
              </v-menu>
              <span class="watched-date ml-2">
                <strong>{{ watched_date }}</strong>
              </span>
            </v-col>
          </v-row>

          <v-row no-gutters class="mb-1">
            <v-col class="d-flex align-items:center">
              <v-rating
                v-model="rating"
                color="yellow"
                background-color="grey"
                size="30"
                :step="0.5"
                :half-increments="true"
              />
              <!-- <span class="rating-number ml-2">{{ rating }}</span> -->
            </v-col>
          </v-row>
        </v-col>
      </v-row>
      <v-row>
        <!-- 리뷰 작성란 -->
        <v-textarea
          v-model="reviewText"
          placeholder="영화에 대한 의견을 작성해주세요."
          rows="3"
          outlined
        ></v-textarea>
      </v-row>
    </v-card-text>

    <v-card-actions>
      <v-spacer></v-spacer>
      <v-btn elevation="5" color="secondary" @click.prevent="reviewCreate">
        작성
      </v-btn>
      <v-btn elevation="5" text> 취소 </v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  props: {
    movie: [Object, Array]
  },
  data() {
    return {
      // 내 정보에 좋아요가 되어있으면, true
      liked: false,
      hearted: false,
      watched: false,
      rating: 0,
      showReviewModal: false,
      reviewText: '',
      // 날짜 받아서 적기
      watched_date: new Date().toISOString().slice(0, 10)
    }
  },
  methods: {
    // 리뷰 제출
    reviewCreate() {
      const movieId = this.movie.id
      const Token = this.myToken
      // console.log(movieId, Token)
      const now = new Date()
      const selectedDate = new Date(this.watched_date)
      selectedDate.setHours(
        now.getHours(),
        now.getMinutes(),
        now.getSeconds(),
        now.getMilliseconds()
      )

      const data = {
        movie: movieId,
        content: this.reviewText,
        rating: this.rating,
        watched: this.watched,
        watched_at: selectedDate
      }
      axios({
        url: `${API_URL}/api/v1/movies/${movieId}/reviews/`,
        method: 'post',
        headers: {
          Authorization: `Bearer ${Token}`
        },
        data
      })
        .then(() => {
          // console.log(res)
          console.log('reviewCreate')
          this.showReviewModal = false
          this.reviewText = ''
          this.$emit('reviewCreate')
        })
        .catch(err => console.log(err))
    },
    cancel() {
      this.showReviewModal = false
    }
  },
  computed: {
    myToken() {
      return this.$store.state.account.accessToken
    }
  }
}
</script>

<style scoped>
.watched-date {
  font-size: 1.1rem;
  margin-left: 0.5rem;
}
.v-dialog > .v-card > .v-card__text {
  padding: 0 24px 0px;
}
</style>
