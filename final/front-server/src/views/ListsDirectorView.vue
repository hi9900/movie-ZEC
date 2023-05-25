<template>
  <v-container>
    {{ movies.director_data.name }} 감독의 영화
    <!-- 나중에 동그라미로 뽑기 -->
    {{ movies.director_data.profile_path }}

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
</style>