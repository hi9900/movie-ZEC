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
      <!-- 각각 갯수 표시 -->
      <div><b>{{ profile.reviews }}</b> 리뷰</div>
       <router-link :to="`/profile/${profile.username}/followers`">
      <div><b>{{ profile.followers }}</b> 팔로워</div>
        </router-link>
          <router-link :to="`/profile/${profile.username}/following`">
      <div><b>{{ profile.following }}</b> 팔로잉</div>
        </router-link>
    </div>


    <div v-if="!isMyProfile">
    <v-btn
    color="primary"
    v-if="!isFollowing"
    @click="follow"
    >
    팔로우
    </v-btn>
    <v-btn
    color="red"
    v-else
    @click="unfollow"
    >
    팔로우 취소
    </v-btn>
    <v-btn
    color="error"
    v-if="!isBlocked"
    @click="blockUser"
    >
    차단하기
    </v-btn>
    <v-btn
    color="success"
    v-else
    @click="unblockUser"
    >
    차단 해제
    </v-btn>
    </div>
    <div v-else> 
      <v-btn>
        회원 정보 수정
      </v-btn>
    </div>

    </v-sheet>
  </v-col>

  <v-col cols="12" md="9">
  <MyProfileData 
  />
  <!-- :profile="profile" -->
</v-col>
    </v-row>
  </v-container>
</template>

<script>
import MyProfileData from "@/components/MyProfileData.vue"


export default {
  name: "UserProfile",
   components: {
    MyProfileData,
  },
  data() {
    return {
      isMyProfile: false,
      profile: {
        profile_image: "https://letterboxd.com/hih1/avatar/medium/",
        username: "hih1",
        reviews: 91,
        ratings: 2382,
        followers: 421,
        following: 341,
        is_staff: false
      },
      isFollowing: false,
      isBlocked: false,
      isAdmin: false,
    };
  },
  methods: {
    // username과 관련된 정보 받아오기
    // getMyProfile(username) {
    //   this.$store.dispatch('profile/getMyProfile', username)
    // },

  //   async blockUser() {
  //   try {
  //     await axios.post(`/api/block-user/${this.profileUserId}`);
  //     this.isBlocked = true;
  //   } catch (error) {
  //     console.error("Error during block:", error);
  //   }
  // },
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
  created() {
    // console.log(this.$route.params.username)
    this.getMyProfile(this.$route.params.username)
    
    // 이 프로필 페이지 정보가 로그인 한 유저 정보와 같은지 확인
    this.isMyProfile = this.$route.params.username === this.authenticatedUser.username

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
