// components/article/ArticleList.vue
<template>
  <v-container>
    <v-row class="mb-5">
      <v-col>
        <v-btn :to="{name: 'ArticleCreate'}" color="primary">
          <!-- @click="openCreateDialog" -->
          새 게시글 작성
        </v-btn>
      </v-col>
    </v-row>
    <v-simple-table>
      <template>
        <thead>
          <tr>
            <th class="text-left">번호</th>
            <th class="text-left">제목</th>
            <th class="text-left">작성자</th>
            <th class="text-left">댓글</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="article in sortedList"
            :key="article.id"
            @click="moveDetail(article.id)"
          >
            <td>{{ article.id }}</td>
            <td>{{ article.title }}</td>
            <td>{{ article.content }}</td>
            <td>{{ article.date }}</td>
          </tr>
        </tbody>
      </template>
    </v-simple-table>
    <article-list-card>
      <!-- <article-list-card
      v-for="article in sortedList"
      :key="article"
      :article="article"
    > -->
    </article-list-card>
  </v-container>
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
    ...mapActions('article', [
      'addArticle',
      'getArticleList',
      'getArticle',
      'getCommentList'
    ]),
    ...mapMutations('article', ['SETARTICLEPAGE']),
    moveDetail(articleId) {
      this.getArticle(articleId)
      this.getCommentList(articleId)
      this.$router.push({name: 'ArticleDetail'})
    }
    // moveDetail() {
    //   this.getArticle(this.article.id)
    //   this.getCommentList(this.article.id)
    //   this.$router.push({name: 'ArticleDetail'})
    // }
  },
  created() {
    this.getArticleList()
  },
  computed: {
    ...mapGetters('article', ['articleList', 'articlePage']),
    ...mapState('article', ['articleList']),
    sortedList() {
      return [...this.articleList].sort((a, b) => a.id - b.id)
    }
  }
}
</script>

<style></style>
