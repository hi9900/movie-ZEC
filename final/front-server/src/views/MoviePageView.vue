<template>
  <v-container>
    <v-row>
      <v-col cols="10">
      <!-- 여긴 검색창 -->
      <!-- 플레이스홀더: 배우, 영화제목을 검색해봐라 -->
      <v-text-field
        v-model="inputMsg"
        filled
        outlined
        rounded
        dense
        @focus="autoSearchList = true"
    >
    </v-text-field>
      </v-col>

      <v-col cols="2">
      <!-- 검색버튼 -->
        <v-btn>
          검색
        </v-btn>
      </v-col>
    </v-row>

    <!-- <v-row>
      여긴 필터
    </v-row>

    <v-row>
      여긴 검색된 갯수
    </v-row> -->

    <v-row>
      <v-col 
        v-for="movie in movieList"
        :key="movie.id"
         cols="12"
            sm="4"
            md="2"
            lg="2">

        <!-- 누르면 각각의 디테일 페이지(DetailView)-> movies/movie.id 로 이동 -->
        <MovieList 
        :movie="movie"
        @click="goToDetail" 
        />
      </v-col>
    </v-row>

    <!-- 페이지네이션 장고연결하고 시도하기 -->
    <!-- <paginate
      :page-count="pageCount"
      :margin-pages="2"
      :click-handler="fetchData"
      :prev-text="'Prev'"
      :next-text="'Next'"
      :container-class="'pagination'"
      :page-class="'page-item'"
      :page-link-class="'page-link'"
      :prev-class="'page-item'"
      :next-class="'page-item'"
      :prev-link-class="'page-link'"
      :next-link-class="'page-link'"
      :disabled-class="'disabled'"
      :active-class="'active'"
    ></paginate> -->
  </v-container>
</template>

<script>
// import axios from 'axios';
// import Paginate from 'vuejs-paginate';
import MovieList from '@/components/MovieList'

export default {
  name: 'MoviePage',
  components: {
    MovieList,
    // Paginate
  },
  data() {
    return {
      inputMsg: '',
      movies: [],
      pageCount: 0,
      currentPage: 1,
      pageSize: 30,
    } 
  },
  computed: {
    movieList() {
      return this.$store.state.movies
    }
  },
  // mounted() {
  //   this.fetchData();
  // },
  methods: {
    // fetchData() {
    //   axios.get(`http://127.0.0.1:8000/movies/?page=${this.currentPage}&page_size=${this.pageSize}`)
    //     .then(response => {
    //       this.movies = response.data;
    //       this.pageCount = Math.ceil(response.headers['x-total-count'] / this.pageSize); // total count를 이용하여 page 개수 계산
    //     })
    //     .catch(error => {
    //       console.log(error);
    //     });
    // },
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  },
  created() {
    this.getMovies()
  },
  
}
</script>

<style scoped>

</style>