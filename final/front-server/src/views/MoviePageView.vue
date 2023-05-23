<template>
  <v-container>
    <!-- 영화 검색 -->
    <MovieSearch
      :searchQuery="searchQuery"
      :MoviesCount="MoviesCount"
      @search="updateSearchQuery"
    />

    <!-- 영화 카드 하나씩 표시 -->
    <!-- 이거 반응형 -->
    <v-row no-gutters>
      <v-col
        v-for="movie in movieList"
        :key="movie.id"
        cols="12"
        sm="4"
        md="4"
        lg="2"
      >
        <MovieList :movie="movie" />
      </v-col>
    </v-row>

    <!-- 맨 끝 없애고 점점 늘어가게 되나? -->
    <!-- 맨앞 맨끝이 안보여도 되고 ...으로 보이게 -->
    <div v-if="totalPages > 1">
      <v-pagination
        v-model="currentPage"
        @input="updateMovie"
        :length="totalPages"
        :total-visible="7"
      ></v-pagination>
    </div>
  </v-container>
</template>

<script>
import MovieSearch from '@/components/movie/MovieSearch'
import MovieList from '@/components/MovieList'
export default {
  name: 'MoviePage',
  components: {
    MovieSearch,
    MovieList
  },
  data() {
    return {
      currentPage: 1,
      searchQuery: ''
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
    }
  },
  watch: {
    searchQuery(query) {
      this.searchQuery = query.trim()
      this.updateMovie()
    }
  },
  methods: {
    updateSearchQuery(query) {
      this.searchQuery = query
      this.currentPage = 1
    },
    // getMovies() {
    //   this.$store.dispatch('movie/getMovies', {
    //     page: this.currentPage,
    //     search: this.searchQuery,
    //   })
    //   window.scrollTo(0, 0)
    // },
    updateMovie() {
      console.log(this.searchQuery)
      this.$store.dispatch('movie/updateMovies', {
        page: this.currentPage,
        search: this.searchQuery
      })
      window.scrollTo(0, 0)
    }
  },
  created() {
    this.updateMovie()
  }
}
</script>

<style scoped>
/* v-pagination__navigation--last {
  display: none;
}
.v-pagination >>> .v-pagination__navigation--last {
  display: none;
} */
</style>