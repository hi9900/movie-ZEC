<template>
  <v-container>
    <!-- 카드쓸건데 그건 이따가 정리해 -->
    <v-card @click="goMovieDetail">
      
    <v-img
    >여긴 포스터</v-img>
    <v-row>{{movie.title}}</v-row>
    <v-row>
      <v-col cols="4">봤어요</v-col>
      <v-col cols="4">좋아요</v-col>
       누르면 리뷰작성창 
      <v-col cols="4">별점</v-col>
    </v-row>
    </v-card>

    <!-- <v-card
    class="mx-auto"
    width="350px"
    max-hight=""
    >
    <v-img
      class="white--text align-end"
      height="200px"
      src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
    >
      <v-card-title>Top 10 Australian beaches</v-card-title>
    </v-img>

    <v-card-subtitle class="pb-0">
      Number 10
    </v-card-subtitle>

    <v-card-text class="text--primary">
      <div>Whitehaven Beach</div>

      <div>Whitsunday Island, Whitsunday Islands</div>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="orange"
        text
      >
        Share
      </v-btn>

      <v-btn
        color="orange"
        text
      >
        Explore
      </v-btn>
    </v-card-actions>
  </v-card> -->

  </v-container>
</template>

<script>
export default {
  props:{
      movie: Object
  },
}

</script>

<style>

</style>