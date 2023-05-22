<template>
<!-- 집가서 이거하기 -->
  <v-skeleton-loader v-if="!randomMovies" type="carousel"></v-skeleton-loader>
  <v-container v-else>
    <v-row>
      <!-- 랜덤 감독 추천 -->
      <v-col cols="12" sm="6" md="4">
        <v-card> 
          <!-- @click="goToDirector(directorMovies.director_data.id)"> -->
          <!-- 카드를 누르면 그 감독의 영화 조회 페이지로 이동 -->
          <v-card-title>{{ directorMovies.director.name }}감독의 영화</v-card-title>
          <v-card-text>
              <div class="poster-container">
              <v-img
                v-for="(movie, index) in directorMovies.data.slice(0, 5)"
                :key="movie.id"
                :src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + movie.poster_path"
                :alt="movie.title"
                class="poster"
                :style="{ zIndex: directorMovies.data.length - index, marginLeft: -index * 20 + 'px' }"
              ></v-img>
            </div>
              <v-col v-if="directorMovies.data.length > 5" cols="4" class="more-movies" >
              </v-col>
          </v-card-text>
        </v-card>
      </v-col>
      <!-- 랜덤 장르 추천 -->
      <!-- 카드를 누르면 그 장르의 영화 조회 페이지로 이동 -->
      <!-- <v-col cols="12" sm="6" md="4">
        <v-card @click="goToGenre(randomMovies.genre_movies.genre.id)">
          <v-card-title>{{ randomMovies.genre_movies.genre.name }}장르의 영화</v-card-title>
          <v-card-text>
              <div class="poster-container">
              <v-img
                v-for="(movie, index) in randomMovies.genre_movies.data.slice(0, 5)"
                :key="movie.id"
                :src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + movie.poster_path"
                :alt="movie.title"
                class="poster"
                :style="{ zIndex: randomMovies.genre_movies.data.length - index, marginLeft: -index * 20 + 'px' }"
              ></v-img>
            </div>
              <v-col v-if="randomMovies.genre_movies.data.length > 5" cols="4" class="more-movies" >
              </v-col>
          </v-card-text>
        </v-card>
      </v-col> -->
    </v-row>

    <v-row>
      <!-- <v-col v-for="list in movieLists" :key="list.id" cols="12" sm="6" md="4">
        <v-card>
          <v-card-title>{{ list.title }}</v-card-title>
          <v-card-text>
              <div class="poster-container">
              <v-img
                v-for="(movie, index) in list.movies.slice(0, 5)"
                :key="movie.id"
                :src="movie.poster"
                :alt="movie.title"
                class="poster"
                :style="{ zIndex: list.movies.length - index, marginLeft: -index * 20 + 'px' }"
              ></v-img>
            </div>
              <v-col v-if="list.movies.length > 5" cols="4" class="more-movies" >
                <v-chip>+{{ list.movies.length - 5 }}</v-chip>
              </v-col>
          </v-card-text>
        </v-card>
      </v-col> -->
    </v-row>
  </v-container>
</template>

<script>

export default {
  name: 'MovieLists',
  data() {
    return {
      // movieLists: []
    }
  },
  computed: {
    directorMovies () {
      return this.$store.state.list.directorMovies
    },
    GenreMovies () {
      return this.$store.state.list.genreMovies
    },
    randomMovies() {
      return this.$store.state.list.randomMovies
    }
  },
  methods: {
    getMovie(){
      this.$store.dispatch('list/getMovie')
      // this.$store.dispatch('list/getDirector'),
      // this.$store.dispatch('list/getGenre')
      // // 동시에 하기엔 너무 느린데; 뷰를 하나로 합치거나 어떤 방법을 찾아야 할 듯
      // axios all 안됨 왜?
      // 안되는게 아니라 너무너무느림
    },
    goToDirector(directorId) {
      this.$router.push({ name: 'Director', params: { directorid: directorId }})
    },
    // goToDirector(directorId) {
    //   this.$router.push({ name: 'Director', params: { directorid: directorId }})
    // }
  },
  created() {
    this.getMovie()
  }
};
</script>

<style>
.poster-container {
  display: flex;
  align-items: flex-start;
}

.poster {
  width: 100px;
  height: auto;
  object-fit: cover;
}
.more-movies {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0;
}
</style>
