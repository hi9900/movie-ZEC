<template>
  <v-container fluid>
    <ReviewDatePicker @selected-date-events="onSelectedDateEvents" />
    <!-- 리뷰 뿌랍 -->
    <div>
      <ul>
        <li v-for="(event, index) in selectedDateEvents" :key="index">
          {{ event.type }}
        </li>
      </ul>
    </div>
  </v-container>
</template>

<script scoped>
import ReviewDatePicker from '@/components/ReviewDatePicker.vue'
export default {
  components: {
    ReviewDatePicker
  },
  data() {
    return {
      selectedDate: '',
      selectedDateEvents: []
    }
  },
  methods: {
    onSelectedDateEvents(date, events) {
      this.selectedDate = date
      this.selectedDateEvents = events
    }
  }
}
</script>
