<template>
  <v-container>
    <v-row v-if="users">
      <v-col cols="3" v-for="user in users" :key="user.id">
        <UserProfileCard @getNewProfile="getNewProfile" :user="user" />
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
  data() {
    return {
      users: []
    }
  },
  computed: {
    // followers() {
    // if (this.profile?.followers !== []) {
    //   return this.profile?.followers
    // }
    // return false
    // }
    followers_count() {
      return this.users.length() > 0
    }
  },
  methods: {
    followers() {
      this.users = this.profile.followers
      // console.log(this.users)
    },
    getNewProfile(username) {
      console.log('follow', username)
      // this.$router.push({name: 'Profile', params: {username: username}})
      this.$emit('getNewProfile', username)
    }
  },
  created() {
    this.followers()
  }
}
</script>
