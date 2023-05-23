<template>
  <v-container>


  <!-- <div v-for="category in categories" :key="category.id"> -->
  <!-- <h2>{{ category.name }}</h2> -->
  <v-container>
    <v-row>
      <!-- 가로로 보이게 바꾸기 -->
      <v-col
        v-for="review in reviews"
        :key="review.id"
        cols="12"
        sm="6"
        md="4"
        lg="3"
      >
        <v-card elevation="2" hover>
          <v-card-title>
            
            {{ review.content }}
            <v-spacer></v-spacer>
            <!-- 이거 날짜만 -->
            {{ review.created_at }}
          </v-card-title>
          <v-card-subtitle>
            <!-- 별로 바꾸기 -->
            Rating: {{ review.rating }}
          </v-card-subtitle>
          <v-card-text>
            작성자 {{ review.user }}
          </v-card-text>
          <v-card-action>
            <!-- 리뷰 좋아요 버튼 -->
            <v-btn> 
               <!-- @click.prevent="like"> -->
              <v-icon>mdi-heart</v-icon>
              {{ review.like_users.length }}
            </v-btn>
          </v-card-action>
        </v-card>
      </v-col>
    </v-row>
  </v-container>


<!-- 
  {{ review.user }}
  {{ review.rating }}
  {{ review.content }}가 있는 데이터 5개
  {{review.like_users|length}} 
  
  -->
<!-- 리뷰 컨텐트를 누르면 리뷰 디테일 뷰로 이동 -->
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
  <!-- </div> -->


  </v-container>

</template>

<script>

export default {
  data() {
    return {
      
       categories: [
      { id: "my-reviews", name: "내가 쓴 리뷰" },
      { id: "following", name: "팔로우한 유저가 쓴 리뷰" },
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
  props: {
    reviews: Array
  },
  methods: {
    
  }
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