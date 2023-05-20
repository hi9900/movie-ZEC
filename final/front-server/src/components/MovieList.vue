<template>
  <v-container>
    <v-card
    class="pa-1" height="100%"
    >
    <v-img
    weight="150px"
    aspect-ratio="0.675"
    :src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + movie.poster_path"
    ></v-img>
    <v-card-title primary-title>{{movie.title}}</v-card-title>
    <v-row>
       <v-card-actions>
        <!-- 이거 연결하기 -->
        <v-btn color="primary" text small>봄</v-btn>
        <v-btn color="primary" text small>좋</v-btn>
        <v-btn color="primary" text small>별점</v-btn>
      </v-card-actions>
    </v-row>
    </v-card>

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