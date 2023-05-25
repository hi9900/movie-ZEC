// article/CommentCreate.vue
<template>
  <form action="">
    <v-text-field v-model="writer" type="text" label="writer"></v-text-field>
    <v-text-field
      v-model="password"
      type="text"
      label="password"
    ></v-text-field>
    <v-text-field v-model="content" type="text" label="content"></v-text-field>
    <v-btn @click="createComment">댓글 달기</v-btn>
  </form>
</template>

<script>
// import axios from 'axios';

import { mapActions } from "vuex";

export default {
  props: ['articleId'],
  data() {
    return {
      writer: '',
      password: '',
      content: ''
    }
  },
  methods: {
    ...mapActions("article", ["addComment", "getCommentList"]),
    async createComment() {
      const comment = {
        writer: this.writer,
        password: this.password,
        content: this.content,
      };
      await this.addComment({ comment, articleId: this.$route.params.articleId });
      this.getCommentList();
      this.$router.push({ name: "ArticleDetail", params: { articleId: this.$route.params.articleId } });
    },
  },
}
</script>

<style></style>