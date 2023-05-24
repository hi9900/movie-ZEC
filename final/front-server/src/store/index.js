import Vue from 'vue'
import Vuex from 'vuex'

// import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
// import router from '../router'

import movie from '@/store/modules/movie.js'
import list from '@/store/modules/list.js'
import account from '@/store/modules/account.js'
import profile from '@/store/modules/profile.js'
import article from '@/store/modules/article.js'

// const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    movie,
    list,
    account,
    profile,
    article
  },
  plugins: [
    createPersistedState({
      paths: ['account']
    })
  ],
  state: {},
  getters: {},
  mutations: {},
  actions: {}
})
