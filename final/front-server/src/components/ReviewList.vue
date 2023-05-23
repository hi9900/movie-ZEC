<template>
  <v-container v-if="!review"></v-container>
  <v-container fluid v-else>
    <v-row>
      <v-col>
        <div class="review">
          <v-row>
            <v-col cols="auto">
              <img
                @click="goToProfile(review.user.username)"
                class="avatar"
                :src="`https://avatars.dicebear.com/api/initials/${review.user}.svg`"
              />
            </v-col>
            <v-col>
              <div class="review-header">
                <div
                  class="review-user"
                  @click="goToProfile(review.user.username)"
                >
                  {{ review.user.username }}
                </div>
                <div class="review-rating">
                  <v-rating
                    :value="review.rating"
                    readonly
                    color="yellow"
                    half-increments
                    background-color="grey darken-1"
                    size="20"
                    dense
                  ></v-rating>
                </div>
                <div class="review-date">
                  {{ formatDate(review.watched_at) }}
                </div>
              </div>
              <div class="review-body" @click="onReview">
                {{ review.content }}
              </div>

              <div class="review-like-icon">
                <v-btn icon @click.prevent="likeReviews">
                  <v-icon :color="isLiked ? 'red' : 'gray'">mdi-heart</v-icon>
                </v-btn>
                {{ like_users_length }}
                <!-- {{ review }} -->
              </div>
            </v-col>
          </v-row>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  data() {
    return {
      like_users_length: this.review.like_users.length,
      isLiked: false
    }
  },
  props: {
    review: Object
  },
  methods: {
    onReview() {
      // 리뷰 단일 페이지로 이동
      console.log(this.review.id)
      this.$router.push({
        name: 'ReviewDetail',
        params: {reviewId: this.review.id}
      })
    },
    formatDate(date) {
      const d = new Date(date)
      return d.toLocaleDateString()
    },
    likeReviews() {
      const Token = this.$store.state.account.accessToken
      // 리뷰에 대한 좋아요, like_users +- 1
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/reviews/${this.review.id}/like/`,
        headers: {
          Authorization: `Bearer ${Token}`
        }
      })
        .then(() => {
          console.log('좋아요/좋아요취소')

          // 이거 좋아요 비동기 어케하지
          // 여기 review.liked_user에 userid가 들어가있는데,
          // 이것도 username으로 바꿔서 만약 그 배열에 있으면 취소, 없으면 좋아요로 구현하기
        })
        .catch(err => {
          console.log(err)
        })
    },
    goToProfile(username) {
      this.$router.push({name: 'Profile', params: {username: username}})
    }
    // isLiked() {}
  }
}
</script>

<style scoped>
.review {
  padding: 1rem;
  /* border: 1px solid #ccc; */ /* 기존 전체 테두리 제거 */
  border-bottom: 1px solid rgba(204, 204, 204, 0.5); /* 아래쪽 테두리 추가 */
  border-radius: 8px;
  margin-bottom: 1rem;
}
.review:hover {
  background-color: rgba(0, 0, 0, 0.03);
}

.review-header {
  display: flex;
  align-items: flex-end;
  flex-wrap: wrap;
}

.avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  margin-top: 0.7rem;
  cursor: pointer;
}

.review-user {
  margin-right: 1rem;
  cursor: pointer;
}

.review-date {
  color: #888;
}

.review-rating {
  margin-top: 8px;
  margin-right: 2rem;
  color: #888;
}

.review-body {
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
  cursor: pointer;
}
.review-like-icon {
  margin-left: 0rem;
  padding-left: 0rem;
}
.avatar {
  cursor: pointer;
}
</style>
