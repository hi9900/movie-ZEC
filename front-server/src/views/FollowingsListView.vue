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
  name: 'FollowingList',
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
  methods: {
    followings() {
      this.users = this.profile?.following
      // console.log(this.users)
    },
    getNewProfile(username) {
      console.log(2)
      this.$emit('getNewProfile', username)
    }
  },
  created() {
    this.followings()
  }
}
</script>
