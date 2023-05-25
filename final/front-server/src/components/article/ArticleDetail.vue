// components/article/ArticleDetail.vue
<template>
  <div>
    {{ article.title }}
    <hr />
    {{ article.content }}
    <hr />
    <div v-for="comment in sortedComments" :key="comment.id">
      {{ comment.content }}
      <hr />
    </div>
    <v-btn :to="{name: 'CreateComment', params: {articleId: article.id}}">
      댓글생성
    </v-btn>
    <v-btn :to="{name: 'ArticleUpdate', params: {articleId: article.id}}">
      게시글 수정
    </v-btn>
    <form @submit.prevent="submitDeleteArticle">
      <!-- <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Delete</button> -->
    </form>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
export default {
  data() {
    return {
      password: ''
    }
  },
  methods: {
    ...mapActions('article', ['deleteArticle']),
    async submitDeleteArticle() {
      try {
        await this.deleteArticle({
          password: this.password,
          articleId: this.$route.params.articleId
        })
        // Clear the password input
        this.password = ''
        // Redirect to article list after successful deletion
        this.$router.push({name: 'ArticleList'})
      } catch (error) {
        console.error(error)
      }
    },
    loadArticle() {
      this.fetchArticle({articleId: this.$route.params.articleId})
    }
  },
  created() {
    this.loadArticle()
  },
  watch: {
    // call again the method if the route changes
    $route: 'loadArticle'
  },
  computed: {
    ...mapGetters('article', ['article', 'commentList']),
    ...mapActions('article', ['deleteArticle']),
    sortedComments() {
      return [...this.commentList].sort((a, b) => a.id - b.id)
    }
  }
}
</script>

<style>
</style>