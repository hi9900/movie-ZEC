<template>
  <v-container fluid>
    <!-- 내가 가진 데이터가 있으면 색칠 하기 -->
    <v-container>
      <v-row>
        <v-col class="py-1">
          <v-btn icon>
            <v-icon @click.prevent="toggleLike" :color="this.like ? 'red' : ''"
              >mdi-heart</v-icon
            >
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="py-1">
          <v-btn @click="toggleWatch" icon class="btn-no">
            <v-icon :color="this.watched ? 'blue' : ''">mdi-eye</v-icon>
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="py-1">
          <v-btn icon @click="showReviewModal = true">
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col class="py-1">
          <v-btn icon @click="sharePage">
            <v-icon>mdi-share-variant</v-icon>
          </v-btn>
        </v-col>
      </v-row>
    </v-container>

    <!-- 리뷰 작성 모달 -->
    <v-dialog v-model="showReviewModal" max-width="600px">
      <ReviewCreate
        :movie="this.movie"
        @cancel="cancel"
        @reviewCreate="reviewCreate"
      />
    </v-dialog>
  </v-container>
</template>

<script>
import ReviewCreate from '@/components/review/ReviewCreate'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  components: {
    ReviewCreate
  },
  data() {
    return {
      like: false,
      watched: false,
      rating: 0,
      showReviewModal: false
    }
  },
  props: {
    movie: [Object, Array],
    myData: [Object],
    myLikeMovies: Array,
    myReviews: Array
  },
  methods: {
    // 영화 좋아요
    toggleLike() {
      const movieId = this.movie.id
      const Token = `Bearer ${this.$store.state.account.accessToken}`
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/movies/${movieId}/like/`,
        headers: {Authorization: Token}
      })
        .then(() => {
          // console.log(res.data)
          this.like = !this.like
          this.$emit('toggleLike')
        })
        .catch(e => console.log(e))
    },
    toggleWatch() {
      // 리뷰를 적은 적 없을때, 봤어요만 추가하는 리뷰 제출
      if (!this.watched) {
        this.watched = !this.watched

        const movieId = this.movie.id
        const Token = this.myToken

        const data = {
          movie: movieId,
          rating: this.rating,
          watched: this.watched
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
            console.log('created review: only watched')
          })
          .catch(e => console.log(e))
      }
    },

    updateWatchedStatus() {
      this.watched = this.rating > 0 || this.reviewText !== ''
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
    },
    liked() {
      if (this.myLikeMovies.length > 0) {
        const movieId = this.movie.id
        const array = this.myLikeMovies

        this.like = array.some(item => item.id === movieId)
      }
    },
    isWatched() {
      const movieId = this.movie.id
      const array = this.myReviews

      this.watched = array.some(item => item.movie.id === movieId)
    },
    reviewCreate() {
      this.showReviewModal = false
      this.$emit('reviewCreate')
    },
    cancel() {
      this.showReviewModal = false
    }
  },
  computed: {
    myToken() {
      return this.$store.state.account.accessToken
    }
  },
  created() {
    this.liked()
    this.isWatched()
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
.btn-no {
  cursor: Default;
}
</style>
