<template>
  <v-container>
    <v-card class="actions-panel__card" tile>
      <v-card-text>
        <v-row no-gutters>
          <v-col cols="6">
            <v-btn icon @click="toggleWatch">
              <!-- 봤어요 -->
              <v-icon :color="WatchIconColor">mdi-eye</v-icon>
            </v-btn>
          </v-col>
          <v-col cols="6">
            <v-btn icon @click="toggleHeart">
              <v-icon :color="heartIconColor">mdi-heart</v-icon>
            </v-btn>
          </v-col>
        </v-row>
        <v-row no-gutters>
          <v-col cols="12">
            <div class="actions-panel__rating text-center">
              <p>영화 평점</p>
              <!-- 왜 삐져나갈까 -->
              <v-rating
                v-model="rating"
                background-color="white"
                size="20"
                :step="0.5"
                :half-increments="true"
              />
            </div>
          </v-col>
        </v-row>
        <v-row no-gutters>
          <!-- 리뷰 작성 모달 띄우기 -->
          <v-col cols="6">
            <v-btn @click="showReviewModal = true">
              리뷰 쓰기
            </v-btn>
          </v-col>
        </v-row>
        <!-- 공유 -->
        <!-- <v-row no-gutters>
          <v-col cols="6">
            <v-btn icon>
              <v-icon>mdi-share-variant</v-icon>
            </v-btn>
          </v-col>
        </v-row> -->
      </v-card-text>

<!-- 리뷰 작성 모달 -->
<!-- 영화 정보 푸랍받아쓰기 -->
<v-dialog v-model="showReviewModal" max-width="600px">
  <v-card>
      <v-card-title>
          리뷰 작성하기
      </v-card-title>
      <v-card-text>
        <v-row >
          <v-col cols="3">
          <!-- 영화 포스터 -->
          <v-img src="moviePoster" alt="영화 포스터" height="150px" width="100px"/>
          </v-col>
          <v-col cols="9">
              <!-- 영화 제목 -->
              <h3>제목</h3>
              <!-- 봤는지 여부, 좋아요 여부 -->
              <v-row>
              <v-btn icon @click="toggleWatch"><v-icon :color="WatchIconColor">mdi-eye</v-icon></v-btn>
              <v-btn icon @click="toggleHeart"><v-icon :color="heartIconColor">mdi-heart</v-icon></v-btn>
              </v-row>
              <!-- 내가 등록한 rating 수정가능 -->
              <v-rating
                v-model="savedRating"
                background-color="white"
                size="20"
                :step="0.5"
                :half-increments="true"
                readonly
              ></v-rating>
              </v-col>
        </v-row>

          <!-- 리뷰 작성란 -->
          <v-textarea
            v-model="reviewText"
            label="당신의 리뷰를 입력해주세요"
            placeholder="영화에 대한 의견을 작성해주세요."
            rows="10"
            outlined
          ></v-textarea>
          <!-- 태그 작성란 -->
          <!-- <v-row class="my-4">
              <v-chip-group
                      column
                      v-model="tagSelection"
                      multiple
                      :mandatory="false">
                  <v-chip
                          v-for="tag in tags"
                          :key="tag"
                  >
                      {{ tag }}
                  </v-chip>
              </v-chip-group>
          </v-row> -->
      </v-card-text>
      <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="darken-1" text @click="submitReview">
              작성하기
          </v-btn>
          <v-btn color="dark--background" text @click="showReviewModal = false">
              취소
          </v-btn>
          
      </v-card-actions>
  </v-card>
    </v-dialog>
    </v-card>

  </v-container>
</template>

<script>
export default {

  data() {
    return {
      liked: false,
      hearted: false,
      watched: false,
      rating: 0,
      showReviewModal: false,
      reviewText: "",
    };
  },
  methods: {
    toggleLike() {
      this.liked = !this.liked
    },
    toggleHeart() {
      this.hearted = !this.hearted
    },
    toggleWatch() {
      this.watched = !this.watched
    },
    submitReview() {
    // 리뷰 제출 로직 구현
    console.log("리뷰 내용:", this.reviewText);
    this.showReviewModal = false;
    this.reviewText = "";
    },
  },
  computed: {
  heartIconColor() {
    return this.hearted ? "red" : "";
  },
  WatchIconColor() {
    return this.watched ? "blue" : ""
  }
  }
}
</script>

<style>
.actions-panel__card {
  max-width: 300px;
  padding: 1rem;
}

.actions-panel__rating {
  flex-direction: column;
  width: 100%;
  align-items: center;
}
</style>