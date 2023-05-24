<template>
  <v-container>
    <v-row v-if="followings">
      <v-col cols="3" v-for="following in this.followings" :key="following.id">
        <UserProfileCard :user="following" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import UserProfileCard from '@/components/profile/UserProfileCard'

export default {
  name: 'FollowingList',
  components: {
    UserProfileCard
  },
  props: {
    profile: Object
  },
  data() {
    return {
      followingList: [
        {
          id: 3,
          username: 'User3',
          profileImage: 'https://via.placeholder.com/150'
        },
        {
          id: 4,
          username: 'User4',
          profileImage: 'https://via.placeholder.com/150'
        }
      ]
    }
  },
  computed: {
    followings() {
      if (this.profile.following !== []) {
        return this.profile?.following
      }
      return false
    }
  }
}
</script>
