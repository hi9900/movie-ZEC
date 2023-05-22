<template>
      <v-container fluid>
        <div v-if="isAdmin">
    <h3>관리자 입니다</h3>
  </div>
        <v-row>
          <v-col cols="12" md="3">
            <v-sheet class="profile-info">
              <v-avatar size="120" class="mx-auto d-block">
                <img :src="profile.profileImage" :alt="profile.name" />
              </v-avatar>
              <h2 class="profile-title">{{ profile.name }}</h2>
              <div class="profile-stats">
                <div><b>{{ profile.reviews }}</b> 리뷰</div>
                <div><b>{{ profile.ratings }}</b> 평점</div>
                <div><b>{{ profile.followers }}</b> 팔로워</div>
                <div><b>{{ profile.following }}</b> 팔로잉</div>
              </div>
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
            </v-sheet>
          </v-col>
          <v-col cols="12" md="9">
  <MyProfileData  />
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
      profile: {
        profileImage: "https://letterboxd.com/hih1/avatar/medium/",
        name: "hih1",
        reviews: 91,
        ratings: 2382,
        followers: 421,
        following: 341,
        bio: "영화에 관한 글을 씁니다.",
      },
      isFollowing: false,
      isBlocked: false,
      isAdmin: false,
    };
  },
  methods: {
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
//   created() {
  // 관리자 여부 확인
//   try {
//     const response = axios.get(`/api/is-admin/${this.profileUserId}`);
//     this.isAdmin = response.data.is_admin;
//   } catch (error) {
//     console.error("Error checking if user is admin:", error);
//   }
// }
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
