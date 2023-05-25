import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
// import router from '@/router'

const profile = {
  namespaced: true,
  state: {
    userReviews: {},
    userData: null,
  },
  getters: {},
  mutations: {
    USER_REVIEWS() { },
    UPDATE_REVIEW() { },

    GET_DATA(state, data) {
      state.userData = data
    }
  },
  actions: {
    // 왜안돼징
    getMyData(context) {
      const Token = `Bearer ${this.$store.state.account.accessToken}`
      const userId = this.$store.state.account.userId

      axios({
        method: 'get',
        url: `${API_URL}/api/v1/user/detail/${userId}/`,
        headers: { Authorization: Token }
      })
        .then((res) => {
          // console.log(res.data)
          context.commit('GET_DATA', res.data)
        })
        .catch(e => console.log(e))
    },

    // updateReview(context, payload) {
    //   axios({
    //     method: 'post',
    // 리뷰 작성 url
    //     url: `${API_URL}`
    //   })
    //   .then((res) => {
    //     console.log(res.data)
    //     context.commit('UPDATE_REVIEW', res.data)
    //   })
    // }
  }
}

export default profile
