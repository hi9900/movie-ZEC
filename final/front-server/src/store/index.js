import Vue from 'vue'
import Vuex from 'vuex'

import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '../router'

import movie from '@/store/modules/movie.js'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)


export default new Vuex.Store({
  modules: {
    movie,
  },
  plugins: [
    createPersistedState(),
  ],
  state: {
    token: null,
  },
  getters: {
    // 로그인
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
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
})
