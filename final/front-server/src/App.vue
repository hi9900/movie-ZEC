<template>
  <v-app :style="appBackgroundStyle">
    <AppBar />
    <v-main>
      <v-container fluid>
        <v-row>
          <v-col cols="1"></v-col>
          <v-col cols="10">
            <router-view/>
          </v-col>
          <v-col cols="1"></v-col>
        </v-row>
      </v-container>
    </v-main>

    <!-- <v-footer app color="footerColor">
      <v-container fluid>
        <v-row>
          <v-col class="text-center">
            <p>&copy; 2023 Company Name. All rights reserved.</p>
          </v-col>
        </v-row>
      </v-container>
    </v-footer> -->
  </v-app>
</template>

<script>
import AppBar from '@/components/AppBar'

export default {
  components: {
    AppBar
  },
  computed: {
    appBackgroundStyle() {
      return `background-color: ${this.$vuetify.theme.themes.dark.background};`;
    }
  }
}
</script>

<style>

</style>