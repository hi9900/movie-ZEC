<template>
  <div>
    <h1>팔로워 목록</h1>
    <div>
      <UserProfileCard v-for="follower in followers" :key="follower.id" :user="follower" />
    </div>
  </div>
</template>

<script>
import UserProfileCard from "@/components/UserProfileCard.vue";

export default {
  name: "FollowersList",
  components: {
    UserProfileCard,
  },
  data() {
    return {
      followers: [
        {
          id: 1,
          username: "User1",
          profileImage: "https://via.placeholder.com/150",
        },
        {
          id: 2,
          username: "User2",
          profileImage: "https://via.placeholder.com/150",
        },
      ],
    };
  },
};
</script>
