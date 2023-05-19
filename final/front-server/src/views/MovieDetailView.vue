<template>
  <v-container>
    <v-row>
      여긴 백드롭 이미지
    </v-row>

      <!-- 이거도 카드로 바꾸기 -->
    <v-row>
      <!-- 얘는 옆에 붙어서 내려도 따라오게 되면 하고 안되면 하지마 -->
      <v-col cols="3">
        <v-row>이건 포스터</v-row>
        <v-row>
          <v-col>봤어요:갯수</v-col>
          <v-col>좋아요:갯수</v-col>
          <v-col>별:총별점</v-col>
        </v-row>
        <v-row>예고편 유투브 API</v-row>
      </v-col>

      <v-col cols="9">
      <v-row>
      <v-col cols="9">
        <v-row>
          여긴 제목
        </v-row>
        <v-row>
          <v-col>여긴 개봉년도</v-col>
          <v-col>여긴 디렉터</v-col>
        </v-row>

        <v-row>여긴 상세</v-row>
        <v-row>
          되면 출연진 정리
        </v-row>
        <v-row>여긴 모얼앳 TMDB</v-row>
      </v-col>

      <v-col cols="3">
        <!-- 리뷰 간단 작성 폼 -->
        <v-row>
          <v-col>봤어요</v-col>
          <v-col>좋아요</v-col>
        </v-row>
        <v-row>
          별점 주기
        </v-row>
        <v-row>
          리뷰 더쓰기
          <!-- 누르면 리뷰를 쓰는 모달창 뜸 -->
        </v-row>
        <v-row>
          공유버튼
        </v-row>
      </v-col>
      </v-row>

      <v-row>
        <!-- 내 리뷰: 있으면 -->
      </v-row>
      <v-row>
        <!-- 친구 리뷰: 있으면  -->
      </v-row>
      <v-row>
        <!-- 인기 리뷰: 좋아요 순 -->
      </v-row>
      <v-row>
        <!-- 최신 리뷰 -->
      </v-row>
      
    </v-col>
    </v-row>
    
  </v-container>
</template>

<script>
export default {

}
</script>

<style>

</style>