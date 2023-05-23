// src/components/MyProfileData.vue

<template>
  <div>
    <ReviewDatePicker @selected-date-events="onSelectedDateEvents" />
    <div>
      <ul>
        <li v-for="(event, index) in selectedDateEvents" :key="index">
          {{ event.type }}
        </li>
      </ul>
    </div>
  </div>
</template>

<script scoped>
import ReviewDatePicker from "@/components/ReviewDatePicker.vue";
export default {
  components: {
    ReviewDatePicker,
  },
  data() {
    return {
      selectedDate: "",
      selectedDateEvents: [],
    };
  },
  methods: {
    onSelectedDateEvents(date, events) {
      this.selectedDate = date;
      this.selectedDateEvents = events;
    },
  },
};
</script>
