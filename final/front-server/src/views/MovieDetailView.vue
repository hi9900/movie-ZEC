<template>
<v-skeleton-loader v-if="!movie" type="carousel"></v-skeleton-loader>
  <v-container v-else>
    
<div class="backdrop-container">
  <v-parallax height="500">
    <div
      class="backdrop-image"
      :style="`background-image: url(https://www.themoviedb.org/t/p/original/${movie.backdrop_path})`"
    >
      <div class="backdrop-fade"></div>
    </div>
  </v-parallax>
</div>

    <!-- 사이 띄우기 -->
    <v-row md="2"></v-row>
        <v-row>
          <v-col md="2" class="poster-container">
            <v-img
          class="movie-poster"
          spect-ratio="0.675"
          :src="'https://www.themoviedb.org/t/p/original/'+`${movie.poster_path}`"
          :lazy-src="'https://www.themoviedb.org/t/p/original/'+`${movie.poster_path}`"
        ></v-img>

        <v-row class="my-2">
          <v-col class="d-flex flex-column align-center">
            <v-icon color="blue">mdi-eye</v-icon>
            <p>갯수</p>
          </v-col>
          <v-col class="d-flex flex-column align-center">
            <v-icon color="red">mdi-heart</v-icon>
            <p>갯수</p>
          </v-col>
          <v-col class="d-flex flex-column align-center">
            <v-icon color="yellow">mdi-star</v-icon>
            <p>갯수</p>
          </v-col>
        </v-row>

        <v-row>
          <v-col>
          <!-- 예고편 유투브 링크 -->
          </v-col>
          </v-row>
          </v-col>

          <v-col md="10">
            <v-row>
          <!-- <v-col md="2"></v-col> -->
          <v-col md="9" no-gutter>
          <v-row>
            <v-col>
            <h1>{{movie.title}}</h1>
            </v-col>
          </v-row>
          <v-row>
          <v-col>
            <v-row>{{movie.release_date}}</v-row>
            <v-row>{{movie.runtime}}</v-row>
          </v-col>
          <v-col>Directed by 
            <p v-for="director in movie.director" :key=director.id>{{director.name}}</p>
            </v-col>
        </v-row>
        <!-- 5줄이 넘어가면 더보기 나중에 구현 -->
        <v-row>
          <v-col>
          <p><strong>Overview:</strong></p>
          {{movie.overview}}
          </v-col>
        </v-row>

        <v-row>
          <v-col no-gutter>
        <p><strong>장르:</strong></p>
          <v-chip-group>
          <v-chip
          :ripple="false" v-for="genre in movie.genres" :key="genre.id">
            {{ genre.name }}
          </v-chip>
          </v-chip-group>
          </v-col>
        </v-row>

        <v-row align="center">
          <v-col>
    <p><strong>키워드:</strong></p>
        <v-chip-group>
          <v-chip
            v-for="keyword in movie.keywords"
            :key="keyword.id"
            color="blue-grey lighten-4"
            small
          >
            {{ keyword.name }}
          </v-chip>
        </v-chip-group>
  </v-col>
        </v-row>

      <v-row align="center">
        <v-col>
          <p><strong>출연진:</strong></p>
          <v-chip-group>
            <v-chip
              v-for="character in movie.characters"
              :key="character.id"
              color="green lighten-4"
              small
            >
              {{ character.actor.name }} - {{ character.character }}
            </v-chip>
          </v-chip-group>
        </v-col>
      </v-row>

        <!-- 여기 유투브 예고편 모달 -->
        <!-- 체크안해봄 -->
          <v-row>
            <v-col>
      <v-btn color="blue" @click="showTrailerModal = true">Watch Trailer</v-btn>
    </v-col>
  </v-row>
  
  <v-dialog v-model="showTrailerModal" width="1000" fullscreen hide-overlay>
    <v-card>
      <v-card-text>
        <iframe width="100%" height="500" :src="`https://www.youtube.com/embed/${youtube_trailer}?autoplay=1`" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="showTrailerModal = false">Close</v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </v-dialog>

        <!-- <v-row>여긴 모얼앳 TMDB</v-row> -->
        </v-col>


        <v-col md="3" no-gutter>
        <!-- 리뷰 간단 작성 폼 -->
        <!-- movie 데이터 푸랍 -->
        <ReviewSimple 
        />
        </v-col>
        </v-row>
        <!-- 여기도 간격 -->
        <ReviewList 
        />
        </v-col>
      </v-row>
        
   
  </v-container>
</template>

<script>
import ReviewSimple from '@/components/ReviewSimple'
import ReviewList from '@/components/ReviewList'
export default {
  components: {
    ReviewSimple,
    ReviewList
  },
  data() {
    return {
      // movie: null,
      // showTrailerModal: false,
      // youtube_trailer: 'abcdefghijklmnop',
    }
  },
  computed: {
    movie() {
      return this.$store.state.movie.movie
    },
  },
  methods: {
    getMovieId(){
      const movieId = this.$route.params.id
      this.$store.dispatch('movie/getMovieId', movieId)
    }
  },
  created() {
    this.getMovieId()
  }
}
</script>

<style scoped>
.backdrop-container {
  position: relative;
}

.backdrop-image {
  position: absolute;
  top: 0;
  width: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
}

/* .backdrop-fade {
    background-image: linear-gradient(90deg,#14181d 0,rgba(20,24,29,.986) .97%,rgba(20,24,29,.945) 2.07833333%,rgba(20,24,29,.883) 3.29666667%,rgba(20,24,29,.803) 4.60166667%,rgba(20,24,29,.711) 5.96666667%,rgba(20,24,29,.61) 7.365%,rgba(20,24,29,.504) 8.77166667%,rgba(20,24,29,.398) 10.16%,rgba(20,24,29,.296) 11.505%,rgba(20,24,29,.203) 12.78%,rgba(20,24,29,.122) 13.95833333%,rgba(20,24,29,.059) 15.01666667%,rgba(20,24,29,.016) 15.92833333%,rgba(20,24,29,0) 16.66666667%,rgba(20,24,29,0) 83.33333333%,rgba(20,24,29,.016) 84.07166667%,rgba(20,24,29,.059) 84.98333333%,rgba(20,24,29,.122) 86.04166667%,rgba(20,24,29,.203) 87.22%,rgba(20,24,29,.296) 88.495%,rgba(20,24,29,.398) 89.84%,rgba(20,24,29,.504) 91.22833333%,rgba(20,24,29,.61) 92.635%,rgba(20,24,29,.711) 94.03333333%,rgba(20,24,29,.803) 95.39833333%,rgba(20,24,29,.883) 96.70333333%,rgba(20,24,29,.945) 97.92166667%,rgba(20,24,29,.986) 99.03%,#14181d),linear-gradient(0deg,#14181d 0,#14181d 21.48148148%,rgba(20,24,29,.986) 23.63703704%,rgba(20,24,29,.945) 26.1%,rgba(20,24,29,.883) 28.80740741%,rgba(20,24,29,.803) 31.70740741%,rgba(20,24,29,.711) 34.74074074%,rgba(20,24,29,.61) 37.84814815%,rgba(20,24,29,.504) 40.97407407%,rgba(20,24,29,.398) 44.05925926%,rgba(20,24,29,.296) 47.04814815%,rgba(20,24,29,.203) 49.88148148%,rgba(20,24,29,.122) 52.5%,rgba(20,24,29,.059) 54.85185185%,rgba(20,24,29,.016) 56.87777778%,rgba(20,24,29,0) 58.51851852%);
    background-repeat: no-repeat;
    content: "";
    display: block;
    height: 675px;
    left: 50%;
    pointer-events: none;
    position: absolute;
    top: 0;
    transform: translateX(-50%);
    width: 1200px;
    z-index: 0;
} */

.poster-container {
  position: sticky;
  top: 0;
  align-self: flex-start;
}
.movie-poster {
  max-width: 100%;
  margin: auto;
}

</style>

