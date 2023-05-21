import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

const movie = {
  namespaced: true,
  state: {
    totalPages: null,
    movies: [],
    movie: [],
    count: null,
  },
  getters: {
    getAllMovies: (state) => state.movies,
    getTotalPages: (state) => state.totalPages,
  },  
  mutations: {
    // MoviePage
    GET_MOVIES(state, movies) {
      state.movies = movies.data
      state.totalPages = movies.total_pages
      state.count = movies.count
    },
    GET_MOVIE(state, movie) {
      state.movie = movie
    },
  },
  actions: {
    getMovies(context, Query) {
      // movie 요청
      // console.log(Query)
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/`,
        params: {
          page: Query.page,
          search: Query.search
        }
      })
      .then((res) => {
        // console.log(res.data, page)
        context.commit('GET_MOVIES', res.data)
      })
      .catch((err) => console.log(err))
    },
    getMovieId(context, movieId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/${movieId}/`
      })
      .then((res) => {
        console.log(res.data)
        context.commit('GET_MOVIE', res.data)
      })
      .catch((err) => console.log(err))
    },
    searchMovies(context, Query) {
      console.log(Query)
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/search/`,
        params: {
          search: Query.search,
          page: Query.page
        }
      })
      .then((res) => {
        console.log(res)
        context.commit('GET_MOVIES', res.data)
      })
      .catch((err) => console.log(err, Query))
    },
  //   filterMovies({ commit }, filter) {
  //     axios({
  //       method: 'get',
  //       url: `${API_URL}/movies/?search=${filter}`
  //     })
  //     .then(res => {
  //       console.log(res.data)
  //         commit('SET_MOVIES', res.data);
  //     })
  //     .catch(error => console.log(error));
  // },
  },
}

export default movie