<template>
  <v-container v-if="!movie" type="carousel"></v-container>
  <v-container fluid v-else>
    <div
      class="backdrop-container"
      :class="`themed-border themetype-${
        $vuetify.theme.dark ? 'dark' : 'light'
      }`"
    >
      <div
        class="backdrop-image"
        :style="`background-image: url(https://www.themoviedb.org/t/p/original/${movie?.backdrop_path})`"
      ></div>
    </div>
    <v-container mt-3>
      <v-row>
        <!-- 영화 정보 왼쪽 플로팅 -->
        <v-col md="2" class="poster-container md-2 hidden-sm-and-down">
          <!-- 영화 포스터 -->
          <v-img
            class="movie-poster"
            spect-ratio="0.675"
            :src="`https://www.themoviedb.org/t/p/original/${movie?.poster_path}`"
          ></v-img>
          <!-- :lazy-src="'https://www.themoviedb.org/t/p/original/'+`${movie.poster_path}`" -->

          <v-row class="mt-2">
            <v-col class="d-flex flex-column align-center">
              <v-icon color="red">mdi-heart</v-icon>
              <p>
                {{ movie.like_users?.length }}
              </p>
            </v-col>
            <v-col class="d-flex flex-column align-center">
              <v-icon color="yellow">mdi-star</v-icon>
              <p>{{ movie.vote_average }}</p>
            </v-col>
          </v-row>

          <!-- 예고편 유투브 링크 모달으로 띄워보기 -->
          <!-- 여기 유투브 예고편 모달 -->
          <!-- 체크안해봄 -->
          <!-- <v-row>
           <v-col>
          <v-row>
            <v-col>
      <v-btn color="blue" @click="showTrailerModal = true">Watch Trailer</v-btn>
    </v-col>
  </v-row>
  
  <v-dialog v-model="showTrailerModal" width="1000" fullscreen hide-overlay>
    <v-card>
      <v-card-text>
        <iframe width="100%" height="500" :src="`https://www.youtube.com/embed/${youtube_trailer}?autoplay=1`" 
        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
        allowfullscreen></iframe>
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn color="primary" text @click="showTrailerModal = false">Close</v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>
    </v-card>
  </v-dialog>
          </v-col> 
          </v-row>-->
        </v-col>

        <v-col xs="12">
          <v-row>
            <v-col>
              <v-row>
                <v-col>
                  <h1>{{ movie.title }}</h1>
                  <p class="text-subtitle-1">
                    {{ movie.original_title }}
                  </p>
                  <span class="text-body-1"
                    >{{ movie.release_date?.substr(0, 4) }}
                  </span>
                  <span class="font-weight-thin">Directed by </span>
                  <span
                    class="text-body-1"
                    v-for="director in movie.director"
                    :key="director.id"
                    >{{ director.name }}
                  </span>
                  <!-- <span>{{ movie.runtime }}M</span> -->
                </v-col>
              </v-row>

              <!-- 5줄이 넘어가면 더보기 -->
              <v-row>
                <v-col>
                  <p class="font-weight-light overview">
                    {{ movie.overview }}
                  </p>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-tabs fixed-tabs color="dark">
                    <v-tab> 장르 </v-tab>
                    <v-tab> 출연 </v-tab>

                    <!-- chip 클릭하면 그거 보러 갈수있게? -->
                    <v-tab-item>
                      <v-card-text>
                        <v-chip
                          class="ma-1"
                          v-for="genre in movie.genres"
                          :key="genre.id"
                        >
                          {{ genre.name }}
                        </v-chip>
                      </v-card-text>
                      <v-card-text>
                        <div
                          v-if="movie.keywords?.length > 0"
                          class="text-caption"
                        >
                          키워드
                        </div>
                        <v-chip
                          class="ma-1"
                          small
                          v-for="keyword in movie.keywords"
                          :key="keyword.id"
                        >
                          {{ keyword.name }}
                        </v-chip>
                      </v-card-text>
                    </v-tab-item>
                    <v-tab-item>
                      <v-card-text>
                        <v-chip
                          class="ma-1"
                          v-for="character in displayedCharacters"
                          :key="character.id"
                        >
                          {{ character.actor.name }}
                          |
                          {{ character.character }}
                        </v-chip>
                        <v-chip
                          :ripple="false"
                          @click="showAll"
                          v-if="!showFullList"
                          >더보기</v-chip
                        >
                      </v-card-text>
                    </v-tab-item>
                  </v-tabs>
                </v-col>
              </v-row>
            </v-col>

            <v-col md="3" no-gutter class="d-none d-md-block">
              <!-- 리뷰 간단 작성 폼 -->
              <!-- movie 데이터 푸랍 -->
              <ReviewSimple :movie="movie" />
            </v-col>
          </v-row>

          <!-- 간격 왜 안생겨 -->
          <v-row>
            <v-col mt-3 class="d-md-none">
              <span>리뷰 작성하기 </span>
              <v-icon class="ml-2">mdi-pencil</v-icon>
            </v-col>
          </v-row>
          <v-row>
            <ReviewList
              :review="review"
              v-for="review in reviews"
              :key="review.id"
            />
          </v-row>
        </v-col>
      </v-row>
    </v-container>
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
      showFullList: false
      // movie: null,
      // showTrailerModal: false,
      // youtube_trailer: 'abcdefghijklmnop',
    }
  },
  computed: {
    movie() {
      return this.$store.state.movie.movie
    },
    reviews() {
      return this.$store.state.movie.reviews
    },
    displayedCharacters() {
      if (this.showFullList) return this.movie.characters
      return this.movie.characters?.slice(0, 10)
    },
    isLogin() {
      return this.$store.getters['accounts/isLogin']
    }
  },
  methods: {
    getMovieId() {
      const movieId = this.$route.params.id
      // console.log(movieId)
      this.$store.dispatch('movie/getMovieId', movieId)
    },
    showAll() {
      this.showFullList = true
    }
  },
  created() {
    this.getMovieId()
  }
}
</script>

<style scoped>
/* .backdrop-container {
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
} */
/* Gradient border */
.backdrop-container {
  position: relative;
  height: 500px;
}

.backdrop-image {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 0;
  width: calc(100% - 16px);
  height: calc(100% - 16px);
  margin: 8px;
  background-repeat: no-repeat;
  background-position: center center;
  background-size: cover;
}

.themetype-dark::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: radial-gradient(
    circle at center,
    rgba(0, 0, 0, 0.6) 0%,
    transparent 70%
  );
}

.themetype-light::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-image: radial-gradient(
    circle at center,
    rgba(255, 255, 255, 0.6) 0%,
    transparent 70%
  );
}

.poster-container {
  position: sticky;
  top: 70px;
  align-self: flex-start;
}
.movie-poster {
  max-width: 100%;
  margin: auto;
}

.overview {
  /* word-break: break-all; */
  word-break: keep-all;
}
</style>

