<template>
  <v-sheet class="profile-info">
    <v-avatar size="120" class="mx-auto d-block">
      <img
        class="avatar"
        :src="`https://source.boringavatars.com/beam/40/${profile?.username}`"
        :alt="profile?.name"
      />
    </v-avatar>
    <h2 class="profile-title">{{ profile?.username }}</h2>

    <div class="profile-stats">
      <div @click.prevent="goToReview" class="stat-item clickable">
        리뷰
        <b>{{ profile?.reviews?.length }}</b>
      </div>
      <div @click.prevent="goToFollower" class="stat-item clickable">
        팔로워 <b>{{ profile?.followers_count }}</b>
      </div>
      <div @click.prevent="goToFollowing" class="stat-item clickable">
        팔로잉 <b>{{ profile?.following_count }}</b>
      </div>
    </div>

    <!-- 내 페이지가 아니면 팔로우버튼 -->
    <div v-if="!this.isMyProfile">
      <v-btn color="primary" outlined v-if="!this.isFollowed" @click="follow">
        팔로우
      </v-btn>
      <v-btn color="red" outlined v-else @click="unfollow"> 팔로우 취소 </v-btn>
    </div>
    <!-- 내 페이지면 수정버튼 -->
    <div v-else>
      <v-btn outlined @click="updateUser"> 회원 정보 수정 </v-btn>
    </div>
  </v-sheet>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ProfileCard',
  props: {
    profile: Object,
    isMyProfile: Boolean,
    isFollowed: Boolean
  },
  methods: {
    goToReview() {
      this.$router.push({name: 'Profile', params: {username: this.profileUser}})
    },
    goToFollower() {
      this.$router.push({
        name: 'FollowersList',
        params: {username: this.profileUser}
      })
    },
    goToFollowing() {
      this.$router.push({
        name: 'FollowingList',
        params: {username: this.profileUser}
      })
    },
    follow() {
      const Token = `Bearer ${this.$store.state.account.accessToken}`

      axios({
        method: 'post',
        url: `${API_URL}/accounts/api/follow/${this.profile.username}/`,
        headers: {Authorization: Token}
      }).then(res => {
        console.log(res)
        this.$emit('follow')
      })
    },
    unfollow() {
      const Token = `Bearer ${this.$store.state.account.accessToken}`

      axios({
        method: 'post',
        url: `${API_URL}/accounts/api/unfollow/${this.profile.username}/`,
        headers: {Authorization: Token}
      }).then(res => {
        console.log(res)
        this.$emit('follow')
      })
    },
    updateUser() {}
  },
  computed: {
    profileUser() {
      return this.profile.username
    }
  }
}
</script>

<style scoped>
.profile-title {
  margin-top: 10px;
  margin-bottom: 20px;
}
.profile-stats div {
  margin-bottom: 5px;
}
.profile-stats {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 1rem;
}
.profile-info {
  text-align: center;
  max-width: 300px;
  margin: 0 auto;
}
.clickable {
  cursor: pointer;
}
.clickable:hover {
  text-decoration: underline;
}
.v-btn:hover {
  background-color: rgba(0, 0, 0, 0.1);
}
</style>