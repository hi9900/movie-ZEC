<!-- diaryTab.vue -->
<template>
  <v-container>
    <v-tabs>
      <v-tab>Diary</v-tab>
      <v-tab-item>
        <v-sheet height="600">
          <v-calendar
            ref="calendar"
            v-model="selectedDate"
            :events="diaryEntries"
            :event-color="getEventColor"
            @click:event="showDiaryEntry"
          ></v-calendar>
        </v-sheet>
        <diary-dialog v-model="dialog" :entry="selectedEntry" />
      </v-tab-item>

      <v-tab>Reviews</v-tab>
      <v-tab-item>
        <v-sheet height="600">
          <v-calendar
            ref="calendar"
            v-model="selectedDate"
            :events="reviews"
            :event-color="getEventColor"
            @click:event="showReview"
          ></v-calendar>
        </v-sheet>
        <review-dialog v-model="dialog" :review="selectedReview" />
      </v-tab-item>
    </v-tabs>
  </v-container>
</template>

<script>
import DiaryDialog from "./DiaryDialog.vue";
import ReviewDialog from "./ReviewDialog.vue";

export default {
  name: "diaryTab",
  components: {
    DiaryDialog,
    ReviewDialog,
  },
  data() {
    return {
      selectedDate: new Date(),
      dialog: false,
      selectedEntry: null,
      selectedReview: null,
      diaryEntries: [
        {
          id: 1,
          title: "할 일 1",
          date: "2022-04-13",
          content: "첫 번째 할 일의 상세 내용입니다.",
          done: false,
        },
        // 기타 다이어리 데이터...
      ],
      reviews: [
        {
          id: 1,
          title: "리뷰 1",
          date: "2022-04-13",
          content: "첫 번째 리뷰의 상세 내용입니다.",
          rating: 5,
        },
        // 기타 리뷰 데이터...
      ],
    };
  },
  methods: {
    showDiaryEntry(event) {
      this.selectedEntry = event;
      this.dialog = true;
    },
    showReview(event) {
      this.selectedReview = event;
      this.dialog = true;
    },
    getEventColor(event) {
      if (event.hasOwnProperty("done")) {
        return event.done ? "green" : "red";
      } else if (event.hasOwnProperty("rating")) {
        return event.rating >= 4 ? "blue" : "orange";
      }
    },
  },
};
</script>
