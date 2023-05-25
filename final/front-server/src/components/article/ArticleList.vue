<template>
  <div>
    <article-list-card
      v-for="article in articleList"
      :key="article"
      :article="article"
    >
    </article-list-card>
    <v-btn :to="{name: 'ArticleCreate'}">생성</v-btn>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapMutations} from 'vuex'
import ArticleListCard from './include/ArticleListCard.vue'
export default {
  components: {ArticleListCard},
  data() {
    return {}
  },
  methods: {
    ...mapActions('article', ['getArticleList']),
    ...mapMutations('article', ['SETARTICLEPAGE'])
  },
  created() {
    this.getArticleList()
  },
  computed: {
    ...mapGetters('article', ['articleList', 'articlePage'])
  }
}
</script>

<style></style>
