<template>
  <v-container>
    <div class="content" v-if="movies.director_data">
      <v-avatar>
        <v-img
          :src="`https://image.tmdb.org/t/p/w500${movies.director_data.profile_path}`"
        ></v-img>
      </v-avatar>
      <span>{{ movies.director_data.name }} 감독의 인기 영화</span>
    </div>
    <!-- {{ movies.director_data.profile_path }} -->
    <v-divider></v-divider>
    <v-row no-gutters>
      <v-col
        v-for="movie in movies.data"
        :key="movie.id"
        cols="12"
        sm="4"
        md="4"
        lg="2"
      >
        <MovieListCard :movie="movie" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import MovieListCard from '@/components/movie/MovieListCard'
export default {
  data() {
    return {}
  },
  components: {
    MovieListCard
  },
  computed: {
    movies() {
      return this.$store.state.list.movies
    }
  },
  methods: {
    getDirectorId() {
      const directorId = this.$route.params.id
      this.$store.dispatch('list/getDirectorId', directorId)
    }
  },
  created() {
    this.getDirectorId()
  }
}
</script>

<style scoped>
.content {
  display: flex;
  align-items: center; /* 수평 정렬 */
  gap: 16px; /* 이미지와 텍스트 사이의 간격 조절 */
  margin-bottom: 24px; /* 밑에 간격 조절 */
}

.image {
  margin: 0;
  padding: 0;
}

.text {
  margin: 0;
  padding: 0;
}
</style>