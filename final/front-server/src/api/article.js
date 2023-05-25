// api/article.js
import { apiInstance } from "./base";

const api = apiInstance();
const base = '/articles/';

function articleList(success, fail) {
  //if (sessionStorage.getItem("accessToken")) {
    const path = `${base}`;
    //api.defaults.headers["Authorization"] = "Bearer " + sessionStorage.getItem("accessToken");
    api.get(path).then(success).catch(fail);
  //}
}

function articleDetail(success, fail, articleId) {
  //if (sessionStorage.getItem("accessToken")) {
    const path = base + articleId + "/";
    //api.defaults.headers["Authorization"] = "Bearer " + sessionStorage.getItem("accessToken");
    api.get(path).then(success).catch(fail);
  //}
}

function articleAdd(success, fail, article) {
  // if (sessionStorage.getItem("accessToken")) {
    const path = `${base}`;
    // api.defaults.headers["Authorization"] = "Bearer " + sessionStorage.getItem("accessToken");
    api.post(path, article)
    .then(success)
    .then(() => articleList(success, fail))
    .catch(fail);
  // }
}

function articleUpadte(success, fail, article, articleId) {
  // if (sessionStorage.getItem("accessToken")) {
    const path = base + articleId + "/";
    // api.defaults.headers["Authorization"] = "Bearer " + sessionStorage.getItem("accessToken");
    api.put(path, article).then(success).catch(fail);
  // }
}

function articleLike(success, fail, article, articleId) {
  // if (sessionStorage.getItem("accessToken")) {
    const path = base + articleId + "/like/";
    // api.defaults.headers["Authorization"] = "Bearer " + sessionStorage.getItem("accessToken");
    api.put(path, article).then(success).catch(fail);
  // }
}

function articleDelete(success, fail, password, articleId) {
  // if (sessionStorage.getItem("accessToken")) {
    const path = base  + articleId + "/";
    // api.defaults.headers["Authorization"] = "Bearer " + sessionStorage.getItem("accessToken");
    api.delete(path, password).then(success).catch(fail);
  // }
}

function commentList(success, fail, articleId) {
 // if (sessionStorage.getItem("accessToken")) {
    const path = `${base}${articleId}/article-comments/`;
    //api.defaults.headers["Authorization"] = "Bearer " + sessionStorage.getItem("accessToken");
    api.get(path).then(success).catch(fail);
  //}
}

function commentAdd(success, fail, comment, articleId) {
  // if (sessionStorage.getItem("accessToken")) {
    const path = base  + articleId + "/article-comments/";
    // api.defaults.headers["Authorization"] = "Bearer " + sessionStorage.getItem("accessToken");
    api.post(path, comment).then(success).catch(fail);
  // }
}

function commentUpdate(success, fail, comment, commentId) {
  // if (sessionStorage.getItem("accessToken")) {
    const path = base + "article-comments/" + commentId + "/";
    // api.defaults.headers["Authorization"] = "Bearer " + sessionStorage.getItem("accessToken");
    api.put(path, comment).then(success).catch(fail);
  // }
}

function commentDelete(success, fail, password, commentId) {
  // if (sessionStorage.getItem("accessToken")) {
    const path = base + "article-comments/" + commentId + "/";
    // api.defaults.headers["Authorization"] = "Bearer " + sessionStorage.getItem("accessToken");
    api.delete(path, password).then(success).catch(fail);
  // }
}

function repliesAdd(success, fail, comment, articleId, commentId) {
  // if (sessionStorage.getItem("accessToken")) {
    const path = base + articleId + "/article-comments/" + commentId + "/replies/";
    // api.defaults.headers["Authorization"] = "Bearer " + sessionStorage.getItem("accessToken");
    api.post(path, comment).then(success).catch(fail);
  // }
}

export { articleList, articleDetail, articleAdd, articleDelete, articleUpadte, articleLike, commentList, commentAdd, commentDelete, commentUpdate, repliesAdd };