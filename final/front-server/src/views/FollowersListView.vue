<template>
  <v-container>
    <v-row v-if="followers()">
      <v-col cols="3" v-for="follower in this.followers" :key="follower.id">
        <UserProfileCard :user="follower" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import UserProfileCard from '@/components/profile/UserProfileCard'

export default {
  name: 'FollowersList',
  components: {
    UserProfileCard
  },
  props: {
    profile: Object
  },
  computed: {
    followers() {
      if (this.profile.followers !== []) {
        return this.profile?.followers
      }
      return false
    }
  },
  method: {}
}
</script>
