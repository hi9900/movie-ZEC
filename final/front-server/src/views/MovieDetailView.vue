<template>
  <v-container>
      <div class="backdrop-container" >
        <!-- 백드롭 이미지 -->
        <!-- 위치, 흐리게 맘에 안들어 -->
        <!-- <v-img :src="'https://image.tmdb.org/t/p/w342/' + '/gPgv2zstVv2uLHIZ3tkb1B1XK82.jpg'"></v-img> -->
        <v-parallax
        class="backdrop-image" 
        src="https://image.tmdb.org/t/p/w1280/gPgv2zstVv2uLHIZ3tkb1B1XK82.jpg"
        height="300"
            >
            </v-parallax>
            <div class="backdrop-mask"></div>
      </div>

    <!-- 사이 띄우기 -->
      <v-container>
        <v-row>
          <v-col md="3" class="poster-container">
            <v-img
          class="movie-poster"
          spect-ratio="0.675"
          src="https://image.tmdb.org/t/p/w342/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg"
          :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
        ></v-img>
        <!-- lazy-src 제대로 바꾸기 -->
        <v-row>
          <!-- 눈모양 -->
          <v-col>봤어요:갯수</v-col>
          <v-col>좋아요:갯수</v-col>
          <v-col>별:총별점</v-col>
        </v-row>
        <!-- <v-row>예고편 유투브 API</v-row> -->
          </v-col>

          <v-col>
            <v-row>
<!-- 세로 사이 띄워주고싶음 -->
          <v-col md="6">
            <!-- 여기에 영화 정보 및 내용을 추가하세요 -->
          <v-row>
            <h1>movie.title</h1>
          </v-row>
          <v-row>
          <v-col>movie.release_date</v-col>
          <v-col>movie -> director</v-col>
        </v-row>
        <!-- 5줄이 넘어가면 더보기 나중에 구현 -->
        <v-row>movie.overview

        </v-row>

        <!-- <v-row>
          되면 출연진 정리
        </v-row> -->
        <!-- <v-row>여긴 모얼앳 TMDB</v-row> -->
        </v-col>

          <v-col md="3">
<!-- 리뷰 간단 작성 폼 -->
<!-- movie 데이터 푸랍 -->
        <ReviewSimple 
        
        />

          </v-col>
        </v-row>
        <!-- 여기도 띄우고 싶은데 -->
        <ReviewList />
        
      
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

}
</script>

<style scoped>
.backdrop-container {
  position: relative;
}
.backdrop-image {
  display: flex;
  justify-content: center;
}
.backdrop-mask {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  /* 테두리 흐리게 어캐해 */
  background: radial-gradient(
    ellipse at center, 
    rgba(255, 255, 255, 0) 30%, 
    #1E252B 100%);
}
.poster-container {
  position: -webkit-sticky;
  position: sticky;
  top: 10px;
}
.movie-poster {
  max-width: 100%;
  margin: auto;
}

</style>