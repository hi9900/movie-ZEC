<template>
  <v-app-bar app color="appBarColor">
    <!-- Logo -->
    <v-img
      @click="goHome"
      max-height="50"
      max-width="150"
      :src="require('@/assets/logo.png')"
      alt="Your Logo"
      class="mr-4 logoImg"
    ></v-img>

    <v-spacer></v-spacer>

    <v-btn text :to="{name: 'Movie'}">Movie</v-btn>
    <v-btn text :to="{name: 'Lists'}">Lists</v-btn>
    <!-- <v-btn text :to="{ name: 'Community' }">Community</v-btn> -->

    <v-btn text v-if="!isLogin" :to="{name: 'LogIn'}">LogIn</v-btn>

    <v-menu v-else open-on-hover offset-y>
      <template v-slot:activator="{on, attrs}">
        <v-btn
          v-if="isLogin"
          text
          v-bind="attrs"
          v-on="on"
          :to="{name: 'Profile', params: {username: username}}"
        >
          Profile
        </v-btn>
      </template>
      <v-list>
        <v-list-item @click.prevent="logout">
          <v-list-item-title>Logout</v-list-item-title>
        </v-list-item>
        <v-list-item @click.prevent="update">
          <v-list-item-title>회원정보수정</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>

    <ModeToggle />
  </v-app-bar>
</template>

<script>
import ModeToggle from '@/components/ModeToggle'
export default {
  name: 'AppBar',
  data() {
    return {
      loggedIn: false
    }
  },
  components: {
    ModeToggle
  },
  computed: {
    isLogin() {
      return this.$store.getters['account/isLogin']
    },
    username() {
      return this.$store.state.account.username
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('account/logout')
      this.$router.push({name: 'Home'})
    },
    goHome() {
      this.$router.push({name: 'Home'})
      // console.log(this.$route.name)
    },
    update() {
      this.$store.dispatch('account/logout')
      this.$router.push({name: 'Update'})
    }
  }
}
</script>

<style scoped>
.logoImg {
  cursor: pointer;
}
.button-padding-left {
  padding-left: 16px;
}
</style>