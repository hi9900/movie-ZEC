import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    articles: [
    ],
    movies: [
      {
      "title": "스텝업6: 이어 오브 더 댄스",
      "original_language": "zh",
      "original_title": "舞出我人生之舞所不能",
      "overview": "재능 있는 스트리트 댄서 ‘타이 호우’는 불미스러운 폭력사건에 휘말려 감옥에 가게 되지만 그 안에서도 실력을 다지며 출소할 날만을 기다린다. 한편 스카이 크루의 리더인 ‘히 추안’은 팀원과의 불화와 부상으로 힘들어 하던 중 사업가 아버지의 건설현장에서 일하며 춤을 연습하고 있는 타이 호우를 눈여겨보고 자신의 팀에 합류를 제안한다. 두 사람은 실력 있는 댄서들을 한데 모아 새로운 스카이 크루를 결성하게 되고 마침내 세계 최강의 댄스 크루 팬텀과의 대결을 앞두게 되는데….",
      "release_date": "2019-07-25",
      "popularity": 14.119,
      "vote_count": 67,
      "vote_average": 6.075,
      "poster_path": "/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg",
      "backdrop_path": "/gPgv2zstVv2uLHIZ3tkb1B1XK82.jpg",
      "runtime": 90,
      "genres": [
          18,
          10402
      ],
      "director": [
          61703
      ],
      "keywords": [
          1691
      ]
  },
      {
      "title": "스텝업6: 이어 오브 더 댄스",
      "original_language": "zh",
      "original_title": "舞出我人生之舞所不能",
      "overview": "재능 있는 스트리트 댄서 ‘타이 호우’는 불미스러운 폭력사건에 휘말려 감옥에 가게 되지만 그 안에서도 실력을 다지며 출소할 날만을 기다린다. 한편 스카이 크루의 리더인 ‘히 추안’은 팀원과의 불화와 부상으로 힘들어 하던 중 사업가 아버지의 건설현장에서 일하며 춤을 연습하고 있는 타이 호우를 눈여겨보고 자신의 팀에 합류를 제안한다. 두 사람은 실력 있는 댄서들을 한데 모아 새로운 스카이 크루를 결성하게 되고 마침내 세계 최강의 댄스 크루 팬텀과의 대결을 앞두게 되는데….",
      "release_date": "2019-07-25",
      "popularity": 14.119,
      "vote_count": 67,
      "vote_average": 6.075,
      "poster_path": "/glrBsRe2SzcL1dNgayNkr6Okbkm.jpg",
      "backdrop_path": "/gPgv2zstVv2uLHIZ3tkb1B1XK82.jpg",
      "runtime": 90,
      "genres": [
          18,
          10402
      ],
      "director": [
          61703
      ],
      "keywords": [
          1691
      ]
  },
],
    token: null,
  },
  getters: {
    // 로그인
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    // MoviePage
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    // 로그인
    // signup & login -> 완료하면 토큰 발급
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({name : 'Home'}) 
      // store/index.js $router 접근 불가 -> import를 해야함
    },
    // 로그아웃
    LOGOUT(state) {
      state.token = null;
    },
  },
  actions: {
    getMovies(context, page) {
      // movie 요청
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
        params: {
          page: page,
        }
      })
      .then((res) => {
        console.log(res.data, context)

        context.commit('GET_MOVIES', res.data)
      })
      .catch((err) => console.log(1, err))
    },
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
        .then((res) => {
          // console.log(res)
          // context.commit('SIGN_UP', res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload) {
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then((res) => {
      context.commit('SAVE_TOKEN', res.data.key)
      })
      .catch((err) => console.log(err))
    },
    logout(context) {
      context.commit('LOGOUT')
    },
  },
  modules: {
  }
})
