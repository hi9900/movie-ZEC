import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
import router from '@/router'


const account = {
  namespaced: true,
  state: {
    token: null,
    accessToken: null,
    refreshToken: null,
    username: '',
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
    },
    SET_ACCESS(state, token){
      state.accessToken = token.access
    },
    SET_REFRESH(state, token) {
      state.refreshToken = token.refresh
    },
    LOGIN(state, token){
      state.accessToken = token.access
      state.refreshToken = token.refresh
      router.push({name : 'Home'})
    },
    // 로그아웃
    LOGOUT(state) {
      state.token = null
    },
    RESET(state){
      state.token = null
      state.accessToken = null
      state.refreshToken = null
    },
    SET_USER(state, username){
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
          email, username, password1, password2
        }
      })
        .then((res) => {
          console.log(res.data)
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
        console.log(err)
      })
    },
    login(context, payload) {
      const email = payload.email
      const password = payload.password
      axios({
        method: 'post',
        url: `${API_URL}/accounts/dj-rest-auth/login/`,
        // url: `${API_URL}/accounts/api/token/`,
        data: {
          email, password
        }
      })
      .then((res) => {
        // 사용자 확인
        console.log('로그인')
        console.log(res)
        context.commit('SAVE_TOKEN', res.data)
        // context.commit('LOGIN', res.data)
        // context.commit('SET_ACCESS', res.data)
        // context.commit('SET_REFRESH', res.data)
      })
      .catch((err) => console.log(err))
    },
    logout(context) {
      context.commit('RESET')
      // axios 요청 안해도 되나?
      // axios({
      //   method: 'delete',
      //   url: `${API_URL}/accounts/dj-rest-auth/logout/`
      // })
      // .then((res) => {
        // console.log('로그아웃')

      //   console.log(res)
      // })
    },
    // 유저정보 가져오기 안돼
    async fetchUser(context) {
      try {
        // 토큰을 헤더에 사용하고 프로필 정보를 얻습니다.
        const res = await axios.get(`${API_URL}/accounts/dj-rest-auth/user/`, {
          headers: { Authorization: `Bearer ${this.state.token}` },
        });
      context.commit('SET_USER', res.data)
    } catch(err) {
      console.log(err)
    }
  },
}
}


export default account
