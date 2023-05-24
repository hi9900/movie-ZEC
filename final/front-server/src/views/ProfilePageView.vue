<template>
  <v-container fluid>
    <div v-if="profile.is_staff">
      <h3>관리자페이지로 이동</h3>
    </div>
    <v-row>
      <v-col cols="12" md="3">
        <v-sheet class="profile-info">
          <v-avatar size="120" class="mx-auto d-block">
            <img :src="profile.profile_image" :alt="profile.name" />
          </v-avatar>
          <h2 class="profile-title">{{ profile.username }}</h2>
          <div class="profile-stats">
            <div>
              <!-- 아직 안줬어 -->
              리뷰 갯수<b>{{ profile.reviews }}</b>
            </div>
            <router-link :to="`/profile/${profile.username}/followers`">
              <div>
                팔로워 <b>{{ profile.followers_count }}</b>
              </div>
            </router-link>
            <router-link :to="`/profile/${profile.username}/following`">
              <div>
                팔로잉 <b>{{ profile.following_count }}</b>
              </div>
            </router-link>
          </div>

          <!-- 내 페이지가 아니면 -->
          <div v-if="!isMyProfile">
            <v-btn color="primary" v-if="!isFollowing" @click="follow">
              팔로우
            </v-btn>
            <v-btn color="red" v-else @click="unfollow"> 팔로우 취소 </v-btn>
            <!-- <v-btn color="error" v-if="!isBlocked" @click="blockUser">
              차단하기
            </v-btn>
            <v-btn color="success" v-else @click="unblockUser">
              차단 해제
            </v-btn> -->
          </div>
          <!-- 내 페이지면 수정 -->
          <div v-else>
            <v-btn> 회원 정보 수정 </v-btn>
          </div>
        </v-sheet>
      </v-col>

      <v-col cols="12" md="9">
        <MyProfileData />
        <!-- 리뷰 뿌랍 -->
        <!-- :profile="profile" -->
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import MyProfileData from '@/components/MyProfileData.vue'
import axios from 'axios'

export default {
  name: 'UserProfile',
  components: {
    MyProfileData
  },
  data() {
    return {
      profile: null
      // profile: {
      //   profile_image: 'https://letterboxd.com/hih1/avatar/medium/',
      //   username: 'hih1',
      //   reviews: 91,
      //   ratings: 2382,
      //   followers: 421,
      //   following: 341,
      //   is_staff: false
      // },
      // isFollowing: false,
      // isBlocked: false,
      // isAdmin: false
    }
  },
  methods: {
    // username과 관련된 정보 받아오기
    getProfile() {
      const Token = this.myToken
      const userId = this.userId
      axios({
        method: 'get',
        url: `http://127.0.0.1:8000/api/v1/user/detail/${userId}/`,
        headers: {
          Authorization: `Bearer ${Token}`
        }
      })
        .then(res => {
          console.log(res.data)
          this.profile = res.data
        })
        .catch(err => console.log(err))
    }
    // getMyProfile(username) {
    //   this.$store.dispatch('profile/getMyProfile', username)
    // },
    // async blockUser() {
    //   try {
    //     await axios.post(`/api/block-user/${this.profileUserId}`)
    //     this.isBlocked = true
    //   } catch (error) {
    //     console.error('Error during block:', error)
    //   }
    // }
    // async unblockUser() {
    //   try {
    //     await axios.post(`/api/unblock-user/${this.profileUserId}`);
    //     this.isBlocked = false;
    //   } catch (error) {
    //     console.error("Error during unblock:", error);
    //   }
    // },
    // async follow() {
    //   try {
    //     await axios.post(`/api/follow/${this.profileUserId}`);
    //     this.isFollowing = true;
    //   } catch (error) {
    //     console.error("Error during follow:", error);
    //   }
    // },
    // async unfollow() {
    //   try {
    //     await axios.post(`/api/unfollow/${this.profileUserId}`);
    //     this.isFollowing = false;
    //   } catch (error) {
    //     console.error("Error during unfollow:", error);
    //   }
    // },
  },
  computed: {
    // 내 페이지인지 확인하기
    isMyProfile() {
      return this.$route.params.username === this.$store.state.account.username
    },
    userId() {
      return this.$store.state.account.userId
    },
    myToken() {
      return this.$store.state.account.accessToken
    }
  },
  created() {
    // console.log(this.$route.params.username)
    this.getProfile()
  }
}
</script>

<style scoped>
.profile-info {
  text-align: center;
}
.profile-title {
  margin-top: 10px;
  margin-bottom: 20px;
}
.profile-stats div {
  margin-bottom: 5px;
}
</style>
