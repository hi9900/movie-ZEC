<template>
  <v-container class="user-row">
    <v-avatar @click="goToProfile(user?.username)">
      <img
        :src="`https://source.boringavatars.com/beam/40/${user?.username}`"
      />
    </v-avatar>
    {{ user?.username }}
  </v-container>

  <!-- <v-list-item-content>
        <v-col>
          <v-list-item-title>
            <router-link :to="`/profile/${user.username}`">{{
              user.username
            }}</router-link>
          </v-list-item-title>
          <p class="follow-info">
            {{ user.followers || 0 }} 팔로워 · {{ user.following || 0 }} 팔로잉
          </p>
        </v-col>
        <v-row>
          <v-col>
            <v-icon color="grey">mdi-comment-outline</v-icon>
            <span class="review-info">{{ user.review || 0 }} 리뷰갯수</span>
          </v-col>
          <v-col>
            <v-icon color="grey">mdi-heart-outline</v-icon>
            <span class="review-info">{{ user.likes || 0 }} 좋아요 갯수</span>
          </v-col>
        </v-row>
      </v-list-item-content> -->
  <!-- <v-list-item-action v-show="!this.itsMe()">
        <v-btn @click="follow" color="primary">팔로우</v-btn>
      </v-list-item-action> -->
</template>

<script>
export default {
  name: 'UserProfileCard',
  props: {
    user: Object
  },
  computed: {
    // itsMe() {
    //   // user 정보가 나이면,
    //   if (this.user?.userId === this.$store.state.account.userId) {
    //     return true
    //   }
    //   return false
    // },
    // isFollowed() {
    // user 정보가 내 팔로우 목록에 있으면 팔로우 한 것임
    // 내 팔로우 목록은 어떻게 가져오지?
    // if (user.userId) {
    // }
    // if (!this.isMyProfile) {
    //   const userId = this.$store.state.account.userId
    //   // profile.followers 안에 userId가 있으면 True
    //   const arr = this.profile.followers
    //   return arr.some(item => item.id === userId)
    // }
    //   return false
    // }
  },
  methods: {
    goToProfile(username) {
      this.$router.push({name: 'Profile', params: {username: username}})
    }
  }
}
</script>

<style scoped>
.follow-info {
  font-size: 14px;
  color: #9e9e9e;
}

.review-info {
  font-size: 14px;
  color: #9e9e9e;
}
.user-row {
  display: flex;
  align-items: center;
  flex-direction: column;
  text-align: center;
}
.user-avatar {
  margin-bottom: 8px;
}
.user-avatar img {
  width: 80px;
  height: 80px;
}
</style>
