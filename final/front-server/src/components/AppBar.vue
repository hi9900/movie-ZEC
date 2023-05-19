<template>
  <v-app-bar app dens color="appBarColor">
      <v-spacer></v-spacer>

      <!-- Logo -->
      <v-img 
        max-height="50"
        max-width="150"
        :src="require('@/assets/logo.png')"
        alt="Your Logo"
        class="mr-4"
      ></v-img>

      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>
      <v-spacer></v-spacer>

      <v-btn text :to="{ name: 'Home' }">Home</v-btn>
      <v-btn text :to="{ name: 'Movie' }">Movie</v-btn>
      <v-btn text :to="{ name: 'Community' }">Community</v-btn>

      <!-- 로그인/프로필 버튼
      로그인 시 상태 변경 해야함 -->
      <!-- <v-btn text :to="{ name: 'Profile' }">Profile</v-btn> -->

      <!-- <v-btn text v-if="!loggedIn" :to="{ name: 'Login' }">Login</v-btn>
      <v-btn text v-else :to="{ name: 'Profile' }">Profile</v-btn> -->
      <v-spacer></v-spacer>
    </v-app-bar>
</template>

<script>
export default {
  name: 'AppBar',
  data() {
    return {
      loggedIn: false,
    }
  }
}
</script>

<style>

</style>