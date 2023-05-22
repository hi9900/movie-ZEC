<template>
  <v-container>
    <v-tabs>
      <v-tab>날짜별</v-tab>
      <v-tab>전체 리뷰</v-tab>

      <v-tab-item>
        <v-row>
          <v-col cols="5">
            <v-date-picker
              v-model="selectedDate"
              :events="eventsForDatePicker"
              :event-color="eventColorResolver"
              @change="dateChanged"
            ></v-date-picker>
            <v-btn color="primary" @click="selectToday">오늘 날짜 선택</v-btn>
          </v-col>
          <v-col cols="7">
            <v-card v-if="selectedReview">
              <v-card-title>{{ selectedReview.title }}</v-card-title>
              <v-card-text>
                {{ selectedReview.date }}<br />
                {{ selectedReview.content }}<br />
                평점: {{ selectedReview.rating }}
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-tab-item>

      <v-tab-item>
        <v-list>
          <v-list-item
            v-for="review in reviews"
            :key="review.id"
            :color="eventColorResolver(review.date)"
          >
            <v-list-item-title>{{ review.title }}</v-list-item-title>
            <v-list-item-subtitle>{{ review.date }}</v-list-item-subtitle>
            <v-list-item-content>{{ review.content }}</v-list-item-content>
            <v-list-item-action>
              평점: {{ review.rating }}
            </v-list-item-action>
          </v-list-item>
        </v-list>
      </v-tab-item>
    </v-tabs>
  </v-container>
</template>

<script>
export default {
  name: "ReviewDatePicker",
  data() {
    return {
      selectedDate: null,
      selectedReview: null,
      reviews: [
        {
          id: 1,
          title: "리뷰 1",
          date: "2023-05-13",
          content: "첫 번째 리뷰의 상세 내용입니다.",
          rating: 5,
          status: "content",
        },
        {
          id: 2,
          title: "리뷰 2",
          date: "2023-05-15",
          content: "두 번째 리뷰의 상세 내용입니다.",
          rating: 3,
          status: "watched",
        },
        // 추가 리뷰 데이터...
      ],
    };
  },
  computed: {
    eventsForDatePicker() {
      return this.reviews.map((review) => review.date);
    },
  },
  methods: {
    dateChanged(date) {
      this.selectedReview = this.reviews.find((review) => review.date === date);
    },
    selectToday() {
      const today = new Date();
      const todayStr = today.toISOString().slice(0, 10);
      this.selectedDate = todayStr;
      this.dateChanged(todayStr);
    },
    eventColorResolver(eventDate) {
      const matchedReview = this.reviews.find(
        (review) => review.date === eventDate
      );
      if (!matchedReview) {
        return null;
      }
      if (matchedReview.status === "watched") {
        return "blue";
      } else if (matchedReview.status === "content") {
        return "green";
      } else if (matchedReview.status === "liked") {
        return "red";
      } else {
        return null;
      }
    },
  },
};
</script>
