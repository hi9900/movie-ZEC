import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
// import router from '@/router'


const profile = {
  namespaced: true,
  state: {
    userReviews: {},
  },
  getters: {
  },
  mutations: {
    USER_REVIEWS() {

    },
    UPDATE_REVIEW() {

    }
  },
  actions: {
    getMyProfile(context, username) {
      axios({
        method: 'get',
        url: `${API_URL}/accounts/users/${username}/`
      })
      .then((res) => {
        console.log(res.data)
      })
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
  },
}

export default profile
