<!-- ReviewDatePicker.vue -->
<template>
  <v-container>
    <v-row>
      <v-col cols="5">
        <v-date-picker
          v-model="selectedDate"
          :events="reviewDatesList"
          event-color="green"
          @change="dateChanged"
        ></v-date-picker>
      </v-col>
      <v-col cols="7">
        <v-card v-if="selectedReview">
          <v-card-title>{{selectedReview.title}}</v-card-title>
          <v-card-text>
            {{selectedReview.date}}<br />
            {{selectedReview.content}}<br />
            평점 : {{selectedReview.rating}}
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
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
        },
        {
          id: 2,
          title: "리뷰 2",
          date: "2023-05-15",
          content: "두 번째 리뷰의 상세 내용입니다.",
          rating: 3,
        },
        // 추가 리뷰 데이터...
      ],
    };
  },
  computed: {
    reviewDatesList() {
      return this.reviews.map((review) => review.date);
    },
  },
  methods: {
    dateChanged(date) {
      this.selectedReview = this.reviews.find((review) => review.date === date);
    },
  },
};
</script>
