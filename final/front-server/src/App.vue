<template>
  <v-app>
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

    <!-- <v-footer color="footerColor">
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
  name: 'App',
  data() {
    return {
      scroll: 0,
      scrollTarget: null
    }
  },
  components: {
    AppBar
  },
  mounted() {
    // goTop을 위해 mount 시 element 설정
    this.scrollTarget = document.getElementById('scroll-target');
  },
  methods: {
      onScroll(e) {
        // 스크롤 움직일 때 마다 호출됨
        this.scroll = e.target.scrollTop;
      },
    goTop() {
      if (this.scrollTarget) {
        this.scrollTarget.scrollTop = 0;
      }
      }
}
}
</script>

<style>

</style>