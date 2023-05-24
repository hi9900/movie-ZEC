<template>
  <div>
    {{article.title}}
    {{article.content}}
    
    <div v-for="comment in commentList" :key="comment.id">
      {{comment.content}}
    </div>
  </div>
</template>

<script>
import {  mapGetters } from 'vuex';
export default {

  data() {
    return {

    };
  },
  methods: {

  },
  created() {

  },
  computed: {
    ...mapGetters("article", ["article", "commentList"]),
  },
}
</script>

<style>

</style>