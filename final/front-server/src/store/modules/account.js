import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import router from '@/router'

const account = {
  namespaced: true,
  state: {
    token: null,
    accessToken: null,
    refreshToken: null,
    userId: '',
    username: '',
    useremail: ''
  },
  getters: {
    // 로그인
    isLogin(state) {
      return state.accessToken ? true : false
    }
  },
  mutations: {
    // 회원가입
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: 'LogIn' })
    },

    SET_ACCESS(state, token) {
      state.accessToken = token.access
    },
    SET_REFRESH(state, token) {
      state.refreshToken = token.refresh
    },
    // 로그인하면 토큰 두개 받아옴
    LOGIN(state, token) {
      state.accessToken = token.access
      state.refreshToken = token.refresh
      state.username = token.username
      state.useremail = token.email
      state.userId = token.id
      router.push({ name: 'Home' })
    },
    // 로그아웃
    LOGOUT(state) {
      state.token = null
    },
    RESET(state) {
      state.token = null
      state.accessToken = null
      state.refreshToken = null
      state.username = ''
      state.useremail = ''
    },
    SET_USER(state, username) {
      state.username = username
    }
  },
  actions: {
    // 회원가입
    signUp(context, payload) {
      const email = payload.email
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method: 'post',
        url: `${API_URL}/accounts/dj-rest-auth/registration/`,
        data: {
          email,
          username,
          password1,
          password2
        }
      })
        .then(res => {
          console.log(res.data)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch(err => {
          console.log(err)
        })
    },
    login(context, payload) {
      const email = payload.email
      const password = payload.password
      axios({
        method: 'post',
        // url: `${API_URL}/accounts/dj-rest-auth/login/`,
        url: `${API_URL}/accounts/api/token/`,
        data: {
          email,
          password
        }
      })
        .then(res => {
          // 사용자 확인
          console.log('로그인')
          console.log(res)
          // context.commit('SAVE_TOKEN', res.data)
          context.commit('LOGIN', res.data)
          // context.commit('SET_ACCESS', res.data)
          // context.commit('SET_REFRESH', res.data)
        })
        .catch(err => console.log(err))
    },
    // 만료된거 확인하고 받아와야함 토큰을 추가로 받아오는 로직

    logout(context) {
      // axios 요청 안해도 되나?

      axios({
        method: 'post',
        url: `${API_URL}/accounts/dj-rest-auth/logout/`
      })
        .then((res) => {
          console.log('로그아웃')

          console.log(res)
          context.commit('RESET')

        })

    },

    // updatePassword() {
    //   axios({
    //     method: 'post',
    //     // url: `${API_URL}/accounts/dj-rest-auth/login/`,
    //     url: `${API_URL}/accounts/api/token/`,
    //     data: {
    //       email, password
    //     }
    //   })
    //     .then((res) => {
    //       // 사용자 확인
    //       console.log('로그인')
    //       console.log(res)
    //       // context.commit('SAVE_TOKEN', res.data)
    //       context.commit('LOGIN', res.data)
    //       // context.commit('SET_ACCESS', res.data)
    //       // context.commit('SET_REFRESH', res.data)
    //     })
    //     .catch((err) => console.log(err))
    // },
  }
}

export default account
