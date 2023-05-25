<template>
  <v-app>
    <AppBar />

    <v-main>
      <v-container fluid>
        <v-row>
          <v-col cols="1"></v-col>
          <v-col cols="10">
            <router-view />
          </v-col>
          <v-col cols="1"></v-col>
        </v-row>
      </v-container>
    </v-main>

    <v-footer color="footerColor">
      <v-container fluid>
        <v-row>
          <v-col class="text-center">
            <p>&copy; 2023 Ssafy 9th BUK 1_HB HY.</p>
          </v-col>
        </v-row>
      </v-container>
    </v-footer>

    <!-- 맨위로 버튼 -->
    <v-fab-transition>
      <v-btn
        v-show="hidden"
        elevation="2"
        bottom
        right
        fab
        fixed
        dark
        color="secondary"
        @click="$vuetify.goTo(0)"
      >
        <v-icon dark>mdi-chevron-up</v-icon>
      </v-btn>
    </v-fab-transition>
  </v-app>
</template>

<script>
import AppBar from '@/components/AppBar'

export default {
  name: 'App',
  data() {
    return {
      fab: false,
      hidden: false,
      offsetTop: 0
    }
  },
  components: {
    AppBar
  },
  methods: {
    handleScroll() {
      this.hidden = window.scrollY > 200 ? true : false
    }
  },
  beforeMount() {
    window.addEventListener('scroll', this.handleScroll)
  },
  beforeDestroy() {
    window.removeEventListener('scroll', this.handleScroll)
  }
}
</script>

<style>
.v-btn--floating {
  /* position: absolute; */

  position: relative;
}
</style>