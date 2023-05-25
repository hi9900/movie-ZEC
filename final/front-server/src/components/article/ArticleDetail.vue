// ArticleDetail.vue
<template>
  <div>
    {{article.title}}
    <hr>
    {{article.content}}
    <hr>
    <div v-for="comment in sortedComments" :key="comment.id">
  {{comment.content}}
   <hr>
  </div>
    <v-btn :to="{name: 'CreateComment', params: { articleId: article.id }}"> 댓글생성 </v-btn>
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
    sortedComments() {
    return [...this.commentList].sort((a, b) => a.id - b.id);
    },
  },
}
</script>

<style>

</style>