<template>
  <v-app-bar app dens color="appBarColor">

      <!-- Logo -->
      <v-img @click="goHome"
        max-height="50"
        max-width="150"
        :src="require('@/assets/logo.png')"
        alt="Your Logo"
        class="mr-4 logoImg"
      ></v-img>

      <v-spacer></v-spacer>

      <v-btn text :to="{ name: 'Movie' }">Movie</v-btn>
      <!-- <v-btn text :to="{ name: 'List' }">Lists</v-btn> -->
      <!-- <v-btn text :to="{ name: 'Community' }">Community</v-btn> -->

      <v-btn text v-if="!isLogin" :to="{ name: 'LogInView' }">LogIn</v-btn>
      <v-btn v-else @click="logout">Logout</v-btn>

      <!-- 로그인/프로필 버튼
      로그인 시 상태 변경 해야함 -->
      <v-btn text :to="{ name: 'Profile' }">Profile</v-btn>

      <!-- <v-btn text v-if="!loggedIn" :to="{ name: 'Login' }">Login</v-btn>
      <v-btn text v-else :to="{ name: 'Profile' }">Profile</v-btn> -->
    </v-app-bar>
</template>

<script>
export default {
  name: 'AppBar',
  data() {
    return {
      loggedIn: false,
    }
  },
  computed: {
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  methods: {
    logout() {
      this.$store.dispatch('logout');
      alert('로그인이 필요한 페이지입니다...')
      this.$router.push({ name: 'LogInView' })
    },
    goHome() {
      // 가드로 바꾸기 -> 누르면 맨 위로 올라가게
      if (this.$route.name !== 'Home'){
      this.$router.push({name: 'Home'})
      // console.log(this.$route.name)
      }
    },
  }
}
</script>

<style>
.logoImg {
  cursor: pointer;
}
</style>