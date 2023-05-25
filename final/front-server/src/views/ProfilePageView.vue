<template>
  <v-container fluid>
    <!-- <div v-if="profile.is_staff">
      <a href="http://127.0.0.1:8000/admin"> <h3>admin</h3></a>
    </div> -->
    <v-row>
      <v-col cols="3">
        <ProfileCard
          :profile="profile"
          :isMyProfile="isMyProfile"
          style="position: sticky; top: 85px"
          @follow="getProfile"
          :isFollowed="isFollowed"
        />
        <!-- style="position: fixed; left: 10px" -->
      </v-col>
      <v-col cols="9">
        <v-tabs center-active>
          <v-tab :to="{name: 'Profile', params: {username: this.profileUser}}">
            Reviews
          </v-tab>
          <v-tab
            :to="{name: 'FollowersList', params: {username: this.profileUser}}"
          >
            Followers
          </v-tab>
          <v-tab
            :to="{name: 'FollowingList', params: {username: this.profileUser}}"
          >
            Followings
          </v-tab>
        </v-tabs>
        <!-- <v-tabs-items v-model="tab">
          <v-tab-item v-for="item in items" :key="item">
            <v-card flat>
              <v-card-text v-text="text"></v-card-text>
            </v-card>
          </v-tab-item>
        </v-tabs-items> -->

        <router-view :profile="profile"></router-view>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

import ProfileCard from '@/components/profile/ProfileCard'

export default {
  name: 'UserProfile',
  components: {
    ProfileCard
  },
  data() {
    return {
      profile: null
    }
  },
  created() {
    // console.log(this.$route.params.username)
    this.getProfile()
  },
  methods: {
    // username과 관련된 정보 받아오기
    getProfile() {
      const Token = this.$store.state.account.accessToken
      const username = this.$route.params.username
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/user/detail/${username}/`,
        headers: {
          Authorization: `Bearer ${Token}`
        }
      })
        .then(res => {
          // console.log(res.data)
          this.profile = res.data
        })
        .catch(err => console.log(err))
    }
  },
  computed: {
    myToken() {
      return this.$store.state.account.accessToken
    },
    profileUser() {
      return this.$route.params.username
    },
    // 내 페이지인지 T/F
    isMyProfile() {
      return this.profileUser === this.$store.state.account.username
    },
    isFollowed() {
      if (!this.isMyProfile) {
        const userId = this.$store.state.account.userId
        // profile.followers 안에 userId가 있으면 True
        const arr = this.profile.followers
        return arr.some(item => item.id === userId)
      }
      return false
    }
  }
}
</script>

<style scoped>
</style>
