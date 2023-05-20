<template>
  <v-app>
    <v-main>
      <v-container fluid>
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
            </v-sheet>
          </v-col>
          <v-col cols="12" md="9">
  <MyProfileData  />
</v-col>
        </v-row>
      </v-container>
    </v-main>
  </v-app>
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
    };
  },
};
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
