<template>
  <div>
    <h1>팔로잉 목록</h1>
    <div>
      <UserProfileCard v-for="following in followingList" :key="following.id" :user="following" />
    </div>
  </div>
</template>

<script>
import UserProfileCard from "@/components/UserProfileCard.vue";

export default {
  name: "FollowingList",
  components: {
    UserProfileCard,
  },
  data() {
    return {
      followingList: [
        {
          id: 3,
          username: "User3",
          profileImage: "https://via.placeholder.com/150",
        },
        {
          id: 4,
          username: "User4",
          profileImage: "https://via.placeholder.com/150",
        },
      ],
    };
  },
};
</script>
