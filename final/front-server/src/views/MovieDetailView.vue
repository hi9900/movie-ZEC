<template>
  <v-container v-if="!movie" type="carousel"></v-container>
  <v-container fluid v-else>
    <div
      v-show="movie.backdrop_path !== 'None'"
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
        <!-- 영화 정보 왼쪽 띄우기 -->
        <v-col md="2" class="poster-container md-2 hidden-sm-and-down">
          <!-- 영화 포스터 -->
          <v-img
            v-show="movie?.poster_path"
            class="movie-poster"
            spect-ratio="0.675"
            :src="`https://www.themoviedb.org/t/p/original/${movie?.poster_path}`"
          ></v-img>
          <!-- 프로젝트 폴더에 로딩 이미지 넣기 -->
          <!-- :lazy-src="'path/to/loading_img.png'" -->
          <!-- 또는 이거? vuetify에 있는데 먼지 모르겟음 -->
          <!-- :lazy-src="'https://www.themoviedb.org/t/p/original/'+`${movie.poster_path}`" -->

          <v-row class="mt-2">
            <v-tooltip top>
              <template v-slot:activator="{on}">
                <v-col v-on="on" class="d-flex flex-column align-center">
                  <v-icon color="red">mdi-heart</v-icon>
                  <p>
                    {{ movie.like_users?.length }}
                  </p>
                </v-col>
              </template>
              <span>liked by {{ movie.like_users?.length }} users</span>
            </v-tooltip>

            <v-tooltip top>
              <template v-slot:activator="{on}">
                <v-col v-on="on" class="d-flex flex-column align-center">
                  <v-icon color="yellow">mdi-star</v-icon>
                  <p>{{ movie.vote_average }}</p>
                </v-col>
              </template>
              <span>vote_average by TMDB</span>
            </v-tooltip>
          </v-row>
        </v-col>

        <v-col xs="12">
          <v-row>
            <v-col>
              <v-row>
                <v-col>
                  <h1>{{ movie?.title }}</h1>
                  <p>
                    <span class="text-subtitle-1">
                      {{ movie?.original_title }}
                    </span>
                    <span>{{ movie?.runtime }}mins</span>
                  </p>
                  <div>
                    <span class="text-body-1"
                      >{{ movie.release_date?.slice(0, 4) }}
                    </span>
                    <span class="font-weight-thin">Directed by </span>
                    <span
                      class="text-body-1"
                      v-for="director in movie?.director"
                      :key="director.id"
                      >{{ director.name }}
                    </span>
                  </div>
                </v-col>
              </v-row>

              <v-row>
                <v-col>
                  <p class="font-weight-light overview">
                    {{ movie?.overview }}
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
          </v-row>
          <v-divider></v-divider>
          <v-container mt-5>
            <!-- content가 있는 리뷰만 보이게 -->

            <!-- {{ reviews }} -->
            <!-- <v-row> 작성된 리뷰 {{ this.review_count }} </v-row> -->

            <v-row no-gutters v-for="review in reviews" :key="review.id">
              <ReviewList v-if="review?.content" :review="review" />
            </v-row>
          </v-container>
          <!-- 글씨 스타일 바꾸기 -->
          <p v-if="reviews.length === 0">이 영화의 첫 리뷰를 작성해보세요</p>
        </v-col>

        <!-- 리뷰 작성 sticky, 폼 -->
        <v-col cols="1" no-gutter class="review-create">
          <ReviewSimpleCreate
            :movie="movie"
            :myData="myData"
            :myLikeMovies="myLikeMovies"
            :myReviews="myData.reviews"
            @reviewCreate="reviewCreate"
            @toggleLike="toggleLike"
          />
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script>
import ReviewSimpleCreate from '@/components/review/ReviewSimpleCreate'
import ReviewList from '@/components/review/ReviewList'
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  components: {
    ReviewSimpleCreate,
    ReviewList
  },
  data() {
    return {
      showFullList: false,
      // movie: null,
      // showTrailerModal: false,
      // youtube_trailer: 'abcdefghijklmnop',
      myData: null,
      review_count: 0
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
    },

    myLikeMovies() {
      return this.myData.like_movies
    }
  },
  methods: {
    toggleLike() {
      this.getMovieId()
    },
    getMovieId() {
      const movieId = this.$route.params.id
      // console.log(movieId)
      this.$store.dispatch('movie/getMovieId', movieId)
    },
    showAll() {
      this.showFullList = true
    },
    reviewCreate() {
      this.getMovieId()
    },
    // 왜안되징
    iscontentReview() {
      const arr = this.reviews
      const res = arr.filter(el => {
        el.content.length > 0
      }).length
      console.log(res)
      this.review_count = res
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
    this.getMovieId()
    this.getMyData()
  }
}
</script>

<style scoped>
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
.review-create {
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
