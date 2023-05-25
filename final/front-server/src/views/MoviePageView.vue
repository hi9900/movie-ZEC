<template>
  <v-container>
    <!-- 영화 검색 -->
    <MovieSearch
      :searchQuery="searchQuery"
      :MoviesCount="MoviesCount"
      @search="updateSearchQuery"
    />
    <div>
      <label>Sort by:</label>
      <v-btn
        v-for="option in options"
        :key="option.value"
        :color="getButtonColor(option)"
        outlined
        class="mx-1"
        @click.prevent="changeSorting(option)"
      >
        {{ option.label }}
        <v-icon v-if="option.value === selectedOption.value" small>
          {{
            option.value !== 'vote_average'
              ? sortOrder === 'desc'
                ? 'mdi-chevron-down'
                : 'mdi-chevron-up'
              : ''
          }}
        </v-icon>
      </v-btn>
    </div>
    <!-- 이거 넘겨주기 -->
    {{ this.myData }}
    <!-- 영화 카드 하나씩 표시 -->
    <v-row no-gutters>
      <v-col
        v-for="movie in movieList"
        :key="movie.id"
        cols="12"
        sm="4"
        md="4"
        lg="2"
      >
        <MovieListCard :movie="movie" />
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
import MovieListCard from '@/components/movie/MovieListCard'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  name: 'MoviePage',
  components: {
    MovieSearch,
    MovieListCard
  },
  data() {
    return {
      currentPage: 1,
      searchQuery: '',
      filter: '',
      sortOrder: 'desc',
      options: [
        {label: 'Popularity', value: 'popularity'},
        {label: 'Release Date', value: 'release_date'},
        {label: 'Runtime', value: 'runtime'},
        {label: 'Vote', value: 'vote_average'}
      ],
      selectedOption: {label: 'Vote', value: 'vote_average'},
      myData: null
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
    },
    filter() {
      this.currentPage = 1
      this.updateMovie()
    }
  },
  methods: {
    getButtonColor(option) {
      return this.selectedOption.value === option.value ? 'blue' : 'grey'
    },
    changeSorting(option) {
      if (option.value !== 'vote_average') {
        if (this.selectedOption.value === option.value) {
          this.sortOrder = this.sortOrder === 'desc' ? 'asc' : 'desc'
        } else {
          this.selectedOption = option
          this.sortOrder = 'desc'
        }
        const sortingOrder = this.sortOrder
        this.filter = this.selectedOption.value + '_' + sortingOrder
      } else {
        this.selectedOption = option
        this.filter = option.value
      }
    },
    // 검색
    updateSearchQuery(query) {
      this.searchQuery = query
      this.currentPage = 1
    },
    // 영화 store.state 가져오기
    updateMovie() {
      this.$store.dispatch('movie/updateMovies', {
        page: this.currentPage,
        search: this.searchQuery,
        ordering: this.filter
      })
      window.scrollTo(0, 0)
    },
    getMyData() {
      const Token = `Bearer ${this.$store.state.account.accessToken}`
      const username = this.$store.state.account.username

      axios({
        method: 'get',
        url: `${API_URL}/api/v1/user/detail/${username}/`,
        headers: {Authorization: Token}
      })
        .then(res => {
          // console.log(res.data)
          this.myData = res.data
        })
        .catch(e => console.log(e))
    }
  },
  created() {
    this.updateMovie()
    this.getMyData()
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