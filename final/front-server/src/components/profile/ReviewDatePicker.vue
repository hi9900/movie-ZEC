<template>
  <v-container fluid>
    <v-row>
      <v-col>
        <v-btn-toggle
          v-model="viewOption"
          @change="onChangeViewOption"
          class="my-3"
          color="blue"
        >
          <v-btn
            density="compact"
            class="mx-1"
            @click="viewOption = 'byDate'"
            value="byDate"
            outlined
          >
            날짜별 리뷰
          </v-btn>
          <v-btn
            density="compact"
            class="mx-1"
            @click="viewOption = 'all'"
            value="all"
            outlined
          >
            전체 리뷰
          </v-btn>
        </v-btn-toggle>
      </v-col>
    </v-row>

    <v-row>
      <v-col cols="5" class="position-relative">
        <div
          class="date-picker-container"
          v-show="this.viewOption === 'byDate'"
        >
          <v-date-picker
            v-model="selectedDate"
            year-icon="mdi-calendar-blank"
            :events="eventsForDatePicker"
            :event-color="eventColorResolver"
            @change="dateChanged"
            color="deep-purple accent-4"
            header-color="deep-purple darken-4"
          ></v-date-picker>
          <v-btn
            class="text-none today-button"
            color="deep-purple accent-1"
            fab
            small
            @click="selectToday"
          >
            <v-icon>mdi-calendar-today</v-icon>
          </v-btn>
        </div>
      </v-col>
      <v-col cols="7">
        {{ reviews[1] }}
        <!-- {{ review.movie }} -->
        <v-row v-for="review in reviews" :key="review.id">
          <ReviewList :review="this.editReviews(review)" />
        </v-row>
        <!-- <v-card v-if="selectedReview">
          <v-card-title>{{ selectedReview.title }}</v-card-title>
          <v-card-text>
            {{ selectedReview.date }}<br />
            {{ selectedReview.content }}<br />
            평점: {{ selectedReview.rating }}
          </v-card-text>
        </v-card> -->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import ReviewList from '@/components/review/ReviewList'

export default {
  name: 'ReviewDatePicker',
  components: {
    ReviewList
  },
  props: {
    reviews: Array
  },
  data() {
    return {
      viewOption: 'byDate',
      selectedDate: null,
      selectedReview: null
    }
  },
  computed: {
    eventsForDatePicker() {
      return this.reviews.map(review => review.date)
    },
    displayedReviews() {
      if (this.viewOption === 'byDate' && this.selectedDate) {
        return this.reviews.filter(review =>
          review.date.startsWith(this.selectedDate)
        )
      } else {
        return this.reviews
      }
    },
    editReviews(review) {
      const data = {
        id: review.id,
        user: {
          username: this.$route.params.username
        },
        rating: review.ration,
        watched_at: review.watched_at,
        content: review.content,
        like_users: review.like_users
      }
      return data
    }
  },
  methods: {
    onChangeViewOption() {
      if (this.viewOption === 'all') {
        this.selectedDate = null
      }
    },
    dateChanged(date) {
      this.selectedReview = this.reviews.find(review => review.date === date)
    },
    selectToday() {
      const today = new Date()
      const todayStr = today.toISOString().slice(0, 10)
      this.selectedDate = todayStr
      this.dateChanged(todayStr)
    },
    eventColorResolver(eventDate) {
      const matchedReview = this.reviews.find(
        review => review.date === eventDate
      )
      if (!matchedReview) {
        return null
      }
      if (matchedReview.status === 'watched') {
        return 'blue'
      } else if (matchedReview.status === 'content') {
        return 'green'
      } else if (matchedReview.status === 'liked') {
        return 'red'
      } else {
        return null
      }
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
.date-picker-container {
  position: relative;
}

.today-button {
  position: absolute;
  top: 15px;
  right: 40px;
}
</style>