<template>
  <v-container>
    
    <!-- <div v-for="(review, index) in reviews" :key="index" class="review">
      <div class="review-header">
        <img class="avatar" :src="review.avatar" alt="Avatar" />
        <div class="review-user">
          <h3>{{review.username}}</h3>
          <v-rating v-model="review.rating" readonly></v-rating>
        </div>
        <div class="review-date">
          {{ review.date }}
        </div>
      </div>
      <div class="review-body">
        {{ review.text }}
      </div>
    </div> -->

    <div v-for="category in categories" :key="category.id">
  <h2>{{ category.name }}</h2>
  <review-list :reviews="allReviews[category.id]" />
</div>

    <!-- 내 리뷰: 있으면 -->
  <!-- <v-row>
    내 리뷰
    <hr>

  </v-row>
  <v-row>
    친구 리뷰 -->
    <!-- 친구 리뷰: 있으면  -->
  <!-- </v-row>
  <v-row>
    인기 리뷰 -->
    <!-- 인기 리뷰: 좋아요 순 -->
  <!-- </v-row>
  <v-row>
    최신 리뷰 -->
    <!-- 최신 리뷰 -->
  <!-- </v-row> -->
  </v-container>

</template>

<script>
export default {
  data() {
    return {
      reviews: [
        {
          username: "ExampleUser1",
          rating: 5,
          date: "1 January 2023",
          text:
            "I absolutely loved this movie! Can't wait for the next one.",
        },
        {
          username: "ExampleUser2",
          rating: 3,
          date: "3 January 2023",
          text:
            "The movie was entertaining, but it didn't live up to the hype.",
        },
      ],
       categories: [
      { id: "my-reviews", name: "내가 쓴 리뷰" },
      { id: "following", name: "팔로우한 유저가 쓴 리뷰" },
      { id: "popular", name: "인기 리뷰" },
      { id: "latest", name: "최신 리뷰" },
    ],
    allReviews: {
      "my-reviews": [
        /* 내가 쓴 리뷰 데이터 */
      ],
      following: [
        /* 팔로우한 유저가 쓴 리뷰 데이터 */
      ],
      popular: [
        /* 인기 리뷰 데이터 */
      ],
      latest: [
        /* 최신 리뷰 데이터 */
      ],
    },
    };
  },
  methods: {
    fetchReviews() {
      // Fetch reviews for the current page from an external API
    },
  },
};
</script>

<style scoped>
* {
  font-size: 14px;
}
.review {
  margin-bottom: 2rem;
  border-bottom: 1px solid #ccc;
  padding-bottom: 1rem;
}

.review-header {
  display: flex;
  align-items: center;
}

.avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  margin-right: 1rem;
}

.review-user {
  margin-right: 2rem;
}

.review-date {
  color: #888;
}

.review-body {
  margin-top: 1rem;
}

h1,
h3 {
  margin: 0;
}
</style>