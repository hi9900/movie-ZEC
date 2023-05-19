<template>
  <v-container>
    <v-row>
      <v-col>
      여긴 검색창
      </v-col>
      <v-col>
        여긴 라디오
      </v-col>
      <v-col>
        여긴 버튼
      </v-col>
    </v-row>
    <v-row>
      여긴 orderby sortby
    </v-row>
    <v-row>
      여긴 검색된 갯수
    </v-row>
    <v-row>
      <v-col v-for="i in 10" :key="i" cols="2"
      
      >
        <!-- 컴포넌트 v-for로 할거야  -->
        <!-- 얘를 누르면 각각의 디테일 페이지(DetailView)로 이동 -->
        <MovieList/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import MovieList from '@/components/MovieList'

export default {
  name: 'MoviePage',
  components: {
    MovieList
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style scoped>

</style>