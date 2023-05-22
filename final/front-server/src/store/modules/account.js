import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import router from '@/router'


const account = {
  namespaced: true,
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
    // 회원가입
    signUp(context, payload) {
      const user_email = payload.user_email
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/dj-rest-auth/registration/`,
        data: {
          user_email, username, password1, password2
        }
      })
        .then((res) => {
          console.log(res)
          // context.commit('SIGN_UP', res.data.key)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload) {
      const user_email = payload.user_email
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          user_email, password
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
}


export default account
