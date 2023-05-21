<template>
  <v-tabs v-model="activeTab">
    <v-tab key="my-reviews">내가 작성한 리뷰</v-tab>
    <v-tab key="liked-movies">내가 좋아요 한 영화</v-tab>
    <v-tab key="watched-movies">내가 봤다고 표시한 영화</v-tab>
    <v-tab key="liked-reviews">내가 좋아요 표시한 리뷰</v-tab>
    <v-tab key="my-movielist">내가 담은 영화 리스트</v-tab>

    <v-tabs-items v-model="activeTab">
      <v-tab-item key="my-reviews">
        <ReviewDatePicker />
        <!-- 여기에 내가 작성한 리뷰 컴포넌트를 추가하세요. -->
      </v-tab-item>
      <v-tab-item key="liked-movies">
        <!-- 여기에 내가 좋아요 한 영화 컴포넌트를 추가하세요. -->
      </v-tab-item>
      <v-tab-item key="watched-movies">
        <!-- 여기에 내가 봤다고 표시한 영화 컴포넌트를 추가하세요. -->
      </v-tab-item>
      <v-tab-item key="liked-reviews">
        <!-- 여기에 내가 좋아요 표시한 리뷰 컴포넌트를 추가하세요.-->
      </v-tab-item>
      <v-tab-item key="my-movielist">
        <!-- 여기에 내가 담은 영화 리스트 컴포넌트를 추가하세요. -->
      </v-tab-item>
    </v-tabs-items>
  </v-tabs>
</template>

<script>
import ReviewDatePicker from '@/components/ReviewDatePicker'
export default {
  name: "MyMoviesReviews",
  components: {
    ReviewDatePicker
  },
  data() {
    return {
      activeTab: "my-reviews",
    };
  },
};
</script>
