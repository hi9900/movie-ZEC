<template>
  <div>
    <article-list-card
      v-for="article in sortedList"
      :key="article"
      :article="article"
    >
    </article-list-card>
    <v-btn :to="{name: 'ArticleCreate'}">생성</v-btn>
  </div>
</template>

<script>
import {mapState, mapActions, mapGetters, mapMutations} from 'vuex'
import ArticleListCard from './include/ArticleListCard.vue'
export default {
  components: {ArticleListCard},
  data() {
    return {}
  },
  methods: {
    ...mapActions('article', ['addArticle','getArticleList']),
    ...mapMutations('article', ['SETARTICLEPAGE'])
  },
  created() {
    this.getArticleList()
  },
  computed: {
    ...mapGetters('article', ['articleList', 'articlePage']),
    ...mapState("article", ["articleList"]),
    sortedList() {
    return [...this.articleList].sort((a, b) => a.id - b.id);
    },
  }
}
</script>

<style></style>
