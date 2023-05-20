<template>
  <v-container>
    <v-calendar ref="calendar" :events="reviews" @click:event="showEventDetails"></v-calendar>
    <v-dialog v-model="eventDialog" max-width="400px">
      <template #activator="{ on, attrs }">
        <v-sheet
          v-if="selectedEvent"
          color="primary"
          dark
          elevation="2"
          v-on="on"
          v-bind="attrs"
        >
          {{ selectedEvent.title }}
        </v-sheet>
      </template>
      <v-card>
        <v-card-title class="text-h5">{{ selectedEvent.title }}</v-card-title>
        <v-card-text>{{ selectedEvent.description }}</v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="eventDialog = false">닫기</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
export default {
  name: "DiaryTab",
  data() {
    return {
      eventDialog: false,
      selectedEvent: null,
      reviews: [
        { title: "영화 리뷰 1", start: "2023-02-01", description: "내용 1" },
        { title: "영화 리뷰 2", start: "2023-02-15", description: "내용 2" },
        // 기타 리뷰 등록 날짜 추가
      ],
    };
  },
  methods: {
    showEventDetails(event) {
      this.selectedEvent = event;
      this.eventDialog = true;
    },
  },
};
</script>
