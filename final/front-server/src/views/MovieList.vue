<template>
  <v-container class="fill-height">
    <h1>오늘의 랜덤 영화 추천</h1>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="6" md="4" no-gutter>
        <v-card
          height="250px"
          outlined
          @click="goToDirector(directorMovies?.director.id)"
        >
          <!-- 카드를 누르면 그 감독의 영화 조회 페이지로 이동 -->
          <v-card-title class="card-title-margin"
            >{{ directorMovies?.director.name }}감독의 인기 영화</v-card-title
          >

          <v-card-text>
            <div class="poster-container">
              <v-img
                aspect-ratio="2/3"
                max-width="100%"
                v-for="(movie, index) in directorMovies?.data.slice(0, 5)"
                :key="movie?.id"
                :src="
                  'https://image.tmdb.org/t/p/w600_and_h900_bestv2' +
                  movie.poster_path
                "
                :alt="movie?.title"
                class="poster"
                :style="{
                  zIndex: directorMovies?.data.length - index,
                  marginLeft: -index * 20 + 'px'
                }"
              ></v-img>
            </div>
            <v-col
              v-if="directorMovies?.data.length > 5"
              cols="4"
              class="more-movies"
            >
            </v-col>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  computed: {
    directorMovies() {
      return this.$store.state.list.directorMovies
    },
    genreMovies() {
      return this.$store.state.list.genreMovies
    },
    actorMovies() {
      return this.$store.state.list.actorMovies
    },
    randomMovies() {
      return this.$store.state.list.randomMovies
    }
    // movielists() {
    //   return this.$store.state.list.movielists
    // }
  },
  methods: {
    getMovie() {
      this.$store.dispatch('list/getMovie')
    },
    goToDirector(directorId) {
      this.$router.push({name: 'ListsDerector', params: {id: directorId}})
    },
    goToGenre(genreId) {
      this.$router.push({name: 'ListsGenre', params: {id: genreId}})
    }
  },
  created() {
    this.getMovie()
    // this.getLists()
  }
}
</script>

<style>
</style>