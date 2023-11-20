<template>
  <v-card height="250px" outlined> 
      <!-- @click="goToDetailList(directorMovies.director_data.id)"> -->
      <!-- 이거 유저 id인데 username을 어케 받아옴 -->
      <v-card-title class="card-title-margin">{{ movielist.user }}의 영화 리스트</v-card-title>
      <v-card-text>
          <div class="poster-container">
          <v-img
          aspect-ratio="2/3"
          max-width="100%"
            v-for="(movie, index) in movielist.movies.slice(0, 5)"
            :key="movie.id"
            :src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + movie.poster_path"
            :alt="movie.title"
            class="poster"
            :style="{ zIndex: movielist.movies.length - index, marginLeft: -index * 20 + 'px' }"
          ></v-img>
        </div>
      </v-card-text>
    </v-card>
</template>

<script>
export default {
  props: {
    movielist: Object,
  },
  created() {
    console.log(this.movielist)
  }
}
</script>

<style scoped>
.poster-container {
  display: flex;
  align-items: flex-start;
}
.poster {
  width: 100px;
  height: 150px;
  object-fit: cover;
}
.card-title-margin {
  margin-bottom: 1rem;
}

.card-text-padding {
  padding-top: 3rem;
}
</style>