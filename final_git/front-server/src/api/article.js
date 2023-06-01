// api/article.js
import { apiInstance } from "./base";

const api = apiInstance();
const base = '/articles/';

function articleList(success, fail) {
  const path = `${base}`;
  api.get(path).then(success).catch(fail);
}

function articleDetail(success, fail, articleId) {
  const path = base + articleId + "/";
  api.get(path).then(success).catch(fail);
}

function articleAdd(success, fail, article) {
  const path = `${base}`;
  api.post(path, article)
    .then(success)
    .then(() => articleList(success, fail))
    .catch(fail);
}

function articleUpdate(success, fail, password, article, articleId) {
  const path = base + articleId + "/";

  // Log the data being sent in the request
  console.log({ password, ...article, articleId });

  api.put(path, { password, ...article })
    .then(success)
    .catch(fail);
}

function articleLike(success, fail, article, articleId) {
  const path = base + articleId + "/like/";
  api.put(path, article).then(success).catch(fail);
}

function articleDelete(success, fail, password, articleId) {
  const path = base + articleId + "/";
  api.delete(path, password).then(success).catch(fail);
}

function commentList(success, fail, articleId) {
  const path = `${base}${articleId}/article-comments/`;
  api.get(path).then(success).catch(fail);
}

function commentAdd(success, fail, comment, articleId) {
  const path = base + articleId + "/article-comments/";
  api.post(path, comment).then(success).catch(fail);
}

function commentUpdate(success, fail, comment, commentId) {
  const path = base + "article-comments/" + commentId + "/";
  api.put(path, comment).then(success).catch(fail);
}

function commentDelete(success, fail, password, commentId) {
  const path = base + "article-comments/" + commentId + "/";
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


export { articleList, articleDetail, articleAdd, articleDelete, articleUpdate, articleLike, commentList, commentAdd, commentDelete, commentUpdate, repliesAdd };