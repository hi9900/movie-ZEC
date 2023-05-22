<template>
  <v-container>
    
    <MovieSearch 
      :searchQuery="searchQuery"
      :MoviesCount="MoviesCount"
      @search="updateSearchQuery"
    />
  <!-- 영화 정보 표시 코드 -->
    <v-row no-gutters>
      <v-col
        v-for="movie in movieList"
        :key="movie.id"
         cols="12"
            sm="4"
            md="4"
            lg="2"
          >
        <MovieList 
        :movie="movie"
        />
      </v-col>
    </v-row>

    <div v-if="totalPages > 1">
       <v-pagination
        v-model="currentPage"
        @input="searchMovies"
        :length="totalPages"
        total-visible="7"
      ></v-pagination>
    </div>
  </v-container>
</template>

<script>

import MovieSearch from '@/components/MovieSearch'
import MovieList from '@/components/MovieList'
export default {
  name: 'MoviePage',
  components: {
    MovieSearch,
    MovieList,
  },
  data() {
    return {
      currentPage: 1,
      searchQuery: '',
      // movieList: null,
      // totalPages: null,
      // MoviesCount: null,
    }
  },
  computed: {
    movieList() {
      return this.$store.state.movie.movies
    },
    totalPages() {
      return this.$store.state.movie.totalPages
    },
    MoviesCount() {
    return this.$store.state.movie.count
  },
  },
  watch: {
    searchQuery(query) {
      this.searchQuery = query.trim()
      this.searchMovies()
    },
  },
  methods: {
    updateSearchQuery(query) {
      this.searchQuery = query;
    },
    // getMovies() {
    //   this.$store.dispatch('movie/getMovies', {
    //     page: this.currentPage,
    //     search: this.searchQuery,
    //   })
    //   window.scrollTo(0, 0)
    // },
    searchMovies() {
    console.log(this.searchQuery)
     this.$store.dispatch('movie/searchMovies', {
        page: this.currentPage,
        search: this.searchQuery,
      })
    window.scrollTo(0, 0)
  },
  },
  created() {
    this.searchMovies()
  },
}
</script>

<style scoped>
</style>