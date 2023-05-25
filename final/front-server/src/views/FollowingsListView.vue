<template>
  <v-container>
    <v-row v-if="users">
      <v-col cols="3" v-for="user in users" :key="user.id">
        <UserProfileCard :user="user" />
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
      console.log(this.users)
    }
  },
  created() {
    this.followings()
  }
}
</script>
