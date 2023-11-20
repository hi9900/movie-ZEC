// store/modules/article.js
import * as api from "@/api/article";
import router from '@/router';

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
    getArticle: ({ commit }, articleId) => {
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
    addArticle: ({ commit, state }, article) => {
      return new Promise((resolve, reject) => {
        api.articleAdd(
          ({ data }) => {
            // console.log(data);
            // Add the new article to the list of articles
            commit("SETARTICLELIST", [...state.articleList, data]);
            resolve(data);
          },
          (error) => {
            console.log(error);
            reject(error);
          },
          article
        );
      });
    },

    updateArticle: (_, { password, article, articleId }) => {
      api.articleUpdate(
        ({ data }) => {
          console.log(data);
        },
        (error) => {
          console.log(error);
        },
        password,
        article,
        articleId
      );
    },

    deleteArticle(_, { articleId, password }) {
      // Call the 'articleDelete' method instead of 'api.delete'
      api.articleDelete(
        () => {
          // Perform some action after the article is deleted, such as redirecting to a different page
          router.push({ name: 'ArticleList' });
        },
        (error) => {
          // Handle error
          console.error(error);
        },
        password,
        articleId
      );
    },
    getCommentList: ({ commit }, articleId) => {
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
    addComment({ commit }, { comment, articleId }) {
      return new Promise((resolve, reject) => {
        api.commentAdd(
          ({ data }) => {
            console.log(commit[0]);
            // commit("UPDATE_COMMENTS", data);
            resolve(data);
          },
          (error) => {
            console.log(error);
            reject(error);
          },
          comment,
          articleId
        );
      });
    },
    // addComment: (comment, articleId) => {
    //   api.commentAdd(
    //     ({ data }) => {
    //       console.log(data);
    //     },
    //     (error) => {
    //       console.log(error);
    //     },
    //     comment,
    //     articleId
    //   )
    // },
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