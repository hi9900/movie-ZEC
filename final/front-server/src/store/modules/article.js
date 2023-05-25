import * as api from "@/api/article";

export default {
  namespaced: true,
  state: {
    articleList: [],
    articleDetail: null,
    commentList: [],
    articlePage: 0,
    commentPage: 0
  },
  getters: {
    articleList(state) {
      return state.articleList;
    },
    article(state) {
      return state.articleDetail;
    },
    commentList(state) {
      return state.commentList;
    },
    articlePage(state) {
      return state.articlePage;
    },
    commentPage(state) {
      return state.commentPage;
    }
  },
  mutations: {
    SETARTICLELIST(state, articleList) {
      state.articleList = articleList;
    },
    SETARTICLE(state, article) {
      state.articleDetail = article;
    },
    SETCOMMENTLIST(state, commentList) {
      state.commentList = commentList;
    },
    SETARTICLEPAGE(state, page) {
      state.articlePage = page;
    },
    SETCOMMENTPAGE(state, page) {
      state.commentPage = page;
    }
  },
  actions: {
    getArticleList: ({ commit }) => {
      api.articleList(
        ({ data }) => {
          commit("SETARTICLELIST", data);
        },
        (error) => {
          console.log(error);
        }
      )
    },
    getArticle: ({commit}, articleId) => {
      api.articleDetail(
        ({ data }) => {
          commit("SETARTICLE", data);
        },
        (error) => {
          console.log(error);
        },
        articleId
      )
    },
    addArticle: (article) => {
      api.articleAdd(
        ({ data }) => {
          console.log(data);
        },
        (error) => {
          console.log(error);
        },
        article
      )
    },
    updateArticle: (article, articleId) => {
      api.articleUpadte(
        ({ data }) => {
          console.log(data);
        },
        (error) => {
          console.log(error);
        },
        article,
        articleId
      )
    },
    deleteArticle: (password, articleId) => {
      api.articleDelete(
        ({ data }) => {
          console.log(data);
        },
        (error) => {
          console.log(error);
        },
        password,
        articleId
      )
    },
    getCommentList: ({commit}, articleId) => {
      api.commentList(
        ({ data }) => {
          commit("SETCOMMENTLIST", data);
        },
        (error) => {
          console.log(error);
        },
        articleId
      )
    },
    addComment: (comment, articleId) => {
      api.commentAdd(
        ({ data }) => {
          console.log(data);
        },
        (error) => {
          console.log(error);
        },
        comment,
        articleId
      )
    },
    updateComment: (comment, commentId) => {
      api.commentUpdate(
        ({ data }) => {
          console.log(data);
        },
        (error) => {
          console.log(error);
        },
        comment,
        commentId
      )
    },
    deleteComment: (password, commentId) => {
      api.commentDelete(
        ({ data }) => {
          console.log(data);
        },
        (error) => {
          console.log(error);
        },
        password,
        commentId
      )
    },
    addreply: (comment, articleId, commentId) => {
      api.repliesAdd(
        ({ data }) => {
          console.log(data);
        },
        (error) => {
          console.log(error);
        },
        comment,
        articleId,
        commentId
      )
    },
  }
}