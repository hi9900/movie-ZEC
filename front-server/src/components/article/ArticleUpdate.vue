// components/article/ArticleUpdate.vue
<template>
  <div>
    <form @submit.prevent="submitUpdateArticle">
      <input v-model="article.writer" type="text" placeholder="Writer" />
      <input v-model="article.title" type="text" placeholder="Title" />
      <input v-model="article.content" type="text" placeholder="Content" />
      <input v-model="password" type="password" placeholder="Password" />
      <button type="submit">Update</button>
    </form>
  </div>
</template>

<script>
import router from '@/router'
import {mapActions} from 'vuex'

export default {
  data() {
    return {
      article: {
        writer: '',
        title: '',
        content: ''
      },
      password: ''
    }
  },
  methods: {
    ...mapActions('article', ['updateArticle']),
    async submitUpdateArticle() {
      try {
        await this.updateArticle({
          password: this.password,
          article: this.article,
          articleId: this.$route.params.articleId
        })
        // redirect to article/list here
        router.push({name: 'ArticleList'}) // replace 'ArticleList' with the actual name of your route
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>