<template>
  <v-container>
    <v-card
      class="card-container pa-1 fixed-height"
      height="100%"
    >
    <div 
    class="movieCard"
    @click="goToDetail(movie.id)">
    <v-img
    hight="200px"
    aspect-ratio="0.675"
    :src="'https://image.tmdb.org/t/p/w600_and_h900_bestv2' + movie.poster_path"
    ></v-img>
      <v-card-title primary-title>
        <div class="ellipsis-second-line">{{ movie.title }}</div>
      </v-card-title>
    </div>

    <v-card-actions class="fixed-bottom">
    <!-- 이거 연결하기 -->
    <v-row no-gutters>
    <v-col cols="4">
      <v-btn color="white" text small>
        <v-icon :color="WatchIconColor? 'blue' : 'white'" @click="toggleEye">mdi-eye</v-icon>
      </v-btn>
    </v-col>
    <v-col cols="4">
      <v-btn color="white" text small>
        <v-icon :color="heartIconColor? 'red' : 'white'" @click="toggleHeart">mdi-heart</v-icon>
      </v-btn>
    </v-col>
    <v-col cols="4">
      <v-btn color="white" text small>
        <v-icon :color="starIconColor? 'yellow' : 'white'" @click="toggleStar">mdi-star</v-icon>
      </v-btn>
    </v-col>
  </v-row>
  </v-card-actions>
    </v-card>

  </v-container>
</template>

<script>
export default {
  props:{
      movie: Object
  },
  data() {
    return {
    // WatchIconColor: false,
    // heartIconColor: false,
    // starIconColor: false,
    }
  },
  methods: {
    goToDetail(movieId) {
      this.$router.push({name: 'MovieDetail', params: {id: movieId}})
    },
    toggleEye() {
      const watched = !this.WatchIconColor
      const payload = {
        movieId: this.movie.id,
        watched,
      }
      this.$store.dispatch('profile/updateReview', payload)
      this.WatchIconColor = watched
  },
  toggleHeart() {
    const liked = !this.heartIconColor
    this.$store.dispatch('profile/updateReview', {
      movieId: this.movie.id,
      liked,
      })
    this.heartIconColor = liked
    },
  toggleStar() {
    const rating = !this.starIconColor ? 3 : 0
      this.$store.dispatch('profile/updateReview', {
        movieId: this.movie.id,
        rating,
      })
      this.starIconColor = rating >= 3
  },
  },
  computed: {
    WatchIconColor() {
      const review = this.$store.getters['profile/userReviews', this.movie.id]
      return review ? review.watched : false;
    },
    heartIconColor() {
      const review = this.$store.getters['profile/userReviews', this.movie.id];
      return review ? review.liked : false;
    },
    starIconColor() {
      const review = this.$store.getters['profile/userReviews', this.movie.id];
      return review ? review.rating >= 3 : false;
    },
  }
}

</script>

<style scoped>
.fixed-height {
  height: 400px;
  min-height: 400px;
  max-height: 400px;
  overflow: hidden;
}
.ellipsis-second-line {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
  overflow: ellipsis;
  text-overflow: ellipsis;
  width: 100%;
  word-wrap: break-word;
  word-break: keep-all;
}
.movieCard {
  cursor: pointer;
}
.card-container {
  position: relative;
}
.fixed-bottom {
  position: absolute;
  bottom: 0;
  width: 100%;
}
</style>