// components/article/include/ArticleListCard.vue
<template>
  <div>
    <div @click="moveDetail()">{{ article.title }}</div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
export default {
  props: {
    article: Object
  },
  methods: {
    ...mapActions('article', ['getArticle', 'getCommentList']),
    moveDetail() {
      this.getArticle(this.article.id)
      this.getCommentList(this.article.id)
      this.$router.push({name: 'ArticleDetail'})
    }
  }
}
</script>

<style>
</style>