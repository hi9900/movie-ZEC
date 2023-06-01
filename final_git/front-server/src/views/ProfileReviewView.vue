<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <v-btn
          v-for="option in options"
          :key="option.value"
          :color="getButtonColor(option)"
          @click="onChangeViewOption(option)"
          outlined
          class="mx-1"
        >
          {{ option.label }}
        </v-btn>
      </v-col>
    </v-row>
    <v-row v-show="this.selectedOption.value === 'all'">
      <v-col>
        리뷰 {{ this.reviews?.length }}
        <!-- 여기 리뷰 -->
        <div
          v-for="review in this.reviews"
          :key="review.id"
          class="d-flex align-center"
          justify="center"
        >
          <v-col cols="1" class="flex-column justify-content-center">
            <v-img
              class="movie-poster mb-3"
              aspect-ratio="0.675"
              :src="`https://www.themoviedb.org/t/p/original/${review.movie.poster_path}`"
            ></v-img>

            <!-- <p>{{ review.movie.title }}</p> -->
          </v-col>

          <v-col cols="8">
            <ReviewList :review="review" />
          </v-col>
        </div>
      </v-col>
    </v-row>

    <v-row v-show="this.selectedOption?.value === 'byDate'">
      <v-col>
        <v-date-picker
          v-model="selectedDate"
          year-icon="mdi-calendar-blank"
          :events="eventsForDatePicker"
        ></v-date-picker>
      </v-col>
      <v-col>
        <!-- {{ selectedDate }} -->
        <!-- {{ this.selectedReview }} -->
        <!-- 여기 리뷰 -->
        리뷰 {{ this.selectedReview.length }}

        <div
          v-for="review in this.selectedReview"
          :key="review.id"
          class="d-flex align-center"
          justify="center"
        >
          <v-col cols="2" class="flex-column justify-content-center">
            <v-img
              class="movie-poster-date mb-3"
              aspect-ratio="0.675"
              :src="`https://www.themoviedb.org/t/p/original/${review.movie.poster_path}`"
            ></v-img>

            <!-- <p>{{ review.movie.title }}</p> -->
          </v-col>
          <v-col>
            <ReviewList :review="review" />
          </v-col>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ReviewList from '@/components/review/ReviewList'

export default {
  name: 'ProfileReviewView',
  props: {
    profile: Object
  },
  components: {
    ReviewList
  },
  data() {
    return {
      selectedDate: new Date().toISOString().slice(0, 10),

      selectedReview: null,
      options: [
        {label: '전체 리뷰', value: 'all'},
        {label: '날짜별 리뷰', value: 'byDate'}
      ],
      selectedOption: {label: '전체 리뷰', value: 'all'},
      // selectedOption: {label: '날짜별 리뷰', value: 'byDate'},
      myData: null
    }
  },
  computed: {
    reviews() {
      return this.profile.reviews
    },
    // today() {
    //   const today = new Date()
    //   const todayStr = new Date().toISOString().slice(0, 10)
    //   return todayStr
    // },
    eventsForDatePicker() {
      return this.reviews.map(review => review.watched_at.slice(0, 10))
    }
    // displayedReviews() {
    //   if (this.viewOption === 'byDate' && this.selectedDate) {
    //     return this.reviews.filter(review =>
    //       review.date.startsWith(this.selectedDate)
    //     )
    //   } else {
    //     return this.reviews
    //   }
    // }
  },
  methods: {
    getButtonColor(option) {
      return this.selectedOption.value === option.value ? 'blue' : 'grey'
    },
    onChangeViewOption(option) {
      this.selectedOption = option
    },
    dateChanged(date) {
      this.selectedReview = this.reviews.filter(
        review => review.watched_at.slice(0, 10) === date
      )
      // console.log(selectedReview)
    },

    // 오늘 선택
    // selectToday() {
    //   const today = new Date()
    //   const todayStr = today.toISOString().slice(0, 10)
    //   this.selectedDate = todayStr
    //   this.dateChanged(todayStr)
    // },
    // 달력에 색깔
    eventColorResolver(eventDate) {
      const matchedReview = this.reviews.find(
        review => review.watched_at.slice(0, 10) === eventDate
      )
      if (!matchedReview) {
        return null
      } else {
        return 'blue'
      }
    }
  },
  created() {
    this.dateChanged(this.selectedDate)
  },
  watch: {
    selectedDate(newDate) {
      this.dateChanged(newDate)
    }
  }
}
</script>

<style scoped>
.custom-radio .v-input__icon::before {
  border-radius: 50%;
  border: 2px solid #3a9dff;
  content: '';
  height: 20px;
  width: 20px;
}
.custom-radio
  .v-input--selection-controls__input:checked
  ~ .v-input__icon::before {
  background-color: #3a9dff;
}
/* .date-picker-container {
  position: relative;
} */

.today-button {
  /* position: absolute; */
  top: 15px;
  right: 40px;
}
.movie-poster {
  max-height: 200px;
  margin: auto;
}
.movie-poster-date {
  max-height: 500px;
  margin: auto;
}
</style>
