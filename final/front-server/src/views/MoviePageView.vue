<template>
  <v-container>
    <v-row>
      <v-col cols="10">
      <!-- 여긴 검색창 -->
      <v-text-field
        v-model="inputMsg"
        filled
        outlined
        rounded
        dense
        @focus="autoSearchList = true"
    >
    </v-text-field>
<!-- <transition name="top-slide" mode="in-out">
      <div class="justify-center align-center flex-column d-flex">
        <v-list class="pa-0 ma-0 search-list" v-show="autoSearchList" light>
          <v-list-item-group>
            
            // 마우스 오버 시 효과를 주기위한 v-hover
            <v-hover v-slot="{ hover }"
                     v-for="(item,index) in completeData"
                     :key="index" 
             >   
             
              // 자동완성 결과값들의 리스트
              <v-list-item
                  class="pa-3 pl-5 top-list"
                  :class="{ 'on-hover': hover }"
                  @click="inputMsg=item.bookTitle"
             >
                
                //내용들
                <v-card
                    class="search-list-img"
                    elevation="1"
                    tile
                >
                  <img
                      :src="item.bookThumb"
                      alt="bookThumb"
                      height="100%"
                      @click="detailView(item.bid)"
                  >
                </v-card>
                
                <v-list-item-content class="pl-8">
                  <v-list-item-title>
                    <span class="search-list-title" @click="detailView(item.bid)"> {{item.bookTitle}} </span>
                  </v-list-item-title>
                  <v-list-item-subtitle class="pt-2">
                    <span class="search-list-subtitle"> {{ item.bookAuthor }} | {{item.bookPublisher}}</span>
                  </v-list-item-subtitle>
                </v-list-item-content>

              </v-list-item>
            </v-hover>

          </v-list-item-group>
        </v-list>
      </div>
    </transition> -->
      </v-col>

      <!-- <v-col cols="5">
        여긴 라디오
      </v-col> -->
      <v-col cols="2">
        <v-btn>
          검색
        </v-btn>
      </v-col>
    </v-row>
    <v-row>
      여긴 orderby sortby
    </v-row>
    <v-row>
      여긴 검색된 갯수
    </v-row>
    <v-row>
      <!-- col 마진 없애기 -->
      <v-col 
        
        v-for="movie in movieList"
        :key="movie.id"
        cols="2">

        <!-- 컴포넌트 v-for로 할거야  -->
        <!-- 얘를 누르면 각각의 디테일 페이지(DetailView)로 이동 -->
        <MovieList :movie="movie"
        @click="goToDetail" 
        />
        <!-- 클릭하면 디테일 페이지로 이동 -->
      </v-col>
    </v-row>

    <!-- 페이지네이션 -->
    <paginate
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
    ></paginate>
  </v-container>
</template>

<script>
// import axios from 'axios';
import Paginate from 'vuejs-paginate';
import MovieList from '@/components/MovieList'

export default {
  name: 'MoviePage',
  components: {
    MovieList,
    Paginate
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