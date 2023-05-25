<template>
  <v-container fluid>
    <v-row>
      <v-col cols="3">
        <!-- 여기부터 -->
        <!-- <v-sheet class="profile-info px-2" style="position: sticky; top: 85px">
          <v-avatar size="120" class="mx-auto d-block">
            <img
              class="avatar"
              :src="`https://source.boringavatars.com/beam/40/${this.profile?.username}`"
              :alt="this.profile?.name"
            />
          </v-avatar>
          <h2 class="profile-title">{{ this.profile?.username }}</h2>

          <div class="profile-stats">
            <div @click.prevent="goToReview" class="stat-item clickable">
              리뷰
              <b>{{ this.profile?.reviews?.length }}</b>
            </div>
            <div @click.prevent="goToFollower" class="stat-item clickable">
              팔로워 <b>{{ this.profile?.followers_count }}</b>
            </div>
            <div @click.prevent="goToFollowing" class="stat-item clickable">
              팔로잉 <b>{{ this.profile?.following_count }}</b>
            </div>
          </div>

          <div v-if="!this.isMyProfile">
            <v-btn
              color="primary"
              outlined
              v-if="!this.isFollowed"
              @click="follow"
            >
              팔로우
            </v-btn>
            <v-btn color="red" outlined v-else @click="unfollow">
              언팔로우
            </v-btn>
          </div>
        </v-sheet> -->
        <!-- 여기까지 -->
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
        <v-tabs loading="true" v-model="tab" center-active>
          <v-tab
            value="reviews"
            :to="{name: 'Profile', params: {username: this.profileUser}}"
          >
            Reviews
          </v-tab>
          <v-tab
            value="followers"
            :to="{name: 'FollowersList', params: {username: this.profileUser}}"
          >
            Followers
          </v-tab>
          <v-tab
            value="followings"
            :to="{name: 'FollowingList', params: {username: this.profileUser}}"
          >
            Followings
          </v-tab>
        </v-tabs>
        <!-- <v-tabs-items v-model="tab">
          <v-tabs-item :value="tab">
            <router-view :profile="profile"></router-view>
          </v-tabs-item>
        </v-tabs-items> -->
        <router-view
          v-if="profile"
          @getNewProfile="getNewProfile"
          :profile="profile"
        ></router-view>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

import ProfileCard from '@/components/profile/ProfileCard'
export default {
  name: 'UserProfile',
  components: {
    ProfileCard
  },
  data() {
    return {
      profile: null,
      tab: 'reviews'
    }
  },
  created() {
    // console.log(this.$route.params.username)
    this.getProfile()
  },
  mounted() {
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
          // this.goToReview()
        })
        .catch(err => console.log(err))
    },
    getNewProfile(username) {
      console.log('mm', username)
      this.$router.push({name: 'Profile', params: {username: username}})
      this.$router.go()
    },

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
    }
  },
  watched: {
    profileUser(newProfile) {
      console.log(11, newProfile)
    }
    // profile(newProfile) {
    //   console.log(11, newProfile)
    // }
  },
  updated() {
    // this.$router.push({name: 'Profile', params: {username: this.profileUser}})
    // this.getProfile()
    // console.log(1111111111111111111111)
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
