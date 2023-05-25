<template>
  <v-container fluid>
    <ReviewDatePicker :reviews="profile.reviews" />
    <!-- @selected-date-events="onSelectedDateEvents" -->
    <!-- 리뷰 뿌랍 -->
    <div>
      <ul>
        <li v-for="(event, index) in selectedDateEvents" :key="index">
          {{ event.type }}
        </li>
        <!-- {{
          profile.reviews
        }} -->
      </ul>
    </div>
  </v-container>
</template>

<script>
import ReviewDatePicker from '@/components/profile/ReviewDatePicker'

export default {
  name: 'ProfileReviewView',
  props: {
    profile: Object
  },
  components: {
    ReviewDatePicker
  },
  data() {
    return {}
  }
}
</script>

<style>
</style>