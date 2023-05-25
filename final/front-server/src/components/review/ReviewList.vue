<template>
  <v-container v-if="!review"></v-container>
  <v-container fluid v-else>
    <v-row>
      <v-col>
        <div class="review">
          <v-row>
            <v-col cols="auto" v-if="review.user.username">
              <img
                @click="goToProfile(review.user.username)"
                class="avatar"
                :src="`https://source.boringavatars.com/beam/40/${review?.user.username}`"
              />
            </v-col>
            <v-col @click="onReview">
              <div class="review-header" style="justify-content: space-between">
                <div v-if="review.user.username" class="review-user">
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
              <div
                class="d-flex align-center"
                style="justify-content: space-between"
              >
                <div class="review-body">
                  {{ review.content }}
                </div>

                <div class="review-like-icon">
                  <v-icon :color="isLiked ? 'red' : 'gray'">mdi-heart</v-icon>
                  {{ like_users_length }}
                </div>
              </div>
            </v-col>
          </v-row>
        </div>
      </v-col>
    </v-row>
    <v-divider></v-divider>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      like_users_length: this.review.like_users.length,
      isLiked: false
    }
  },
  props: {
    review: Object,
    profile: Object
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

    goToProfile(username) {
      this.$router.push({name: 'Profile', params: {username: username}})
    }
    // isLiked() {}
  },
  computed: {
    // username() {
    //   if (this.review.user.username) {
    //     return this.review.user.username
    //   } else {
    //     return this.profile.username
    //   }
    // }
  }
}
</script>

<style scoped>
.review {
  padding: 1rem;
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
