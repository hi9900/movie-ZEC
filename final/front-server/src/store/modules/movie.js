import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

const movie = {
  namespaced: true,
  state: {
    totalPages: null,
    movies: [],
    movie: [],
    count: null,
    genres: [],
    reviews: [],
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
    GET_REVIEWS(state, review) {
      state.reviews = review
    }
  },
  actions: {
    getMovieId(context, movieId) {
    axios
    .all([
      axios.get(`${API_URL}/api/v1/movies/${movieId}/`), 
      axios.get(`${API_URL}/api/v1/movies/${movieId}/reviews/`)
    ])
    .then(
      axios.spread((res1, res2) => {
      console.log(res1.data, res2.data)
      context.commit('GET_MOVIE', res1.data)
      context.commit('GET_REVIEWS', res2.data)
    })
    )
    .catch((err) => console.log(err))
  },
    // 영화 단일 조회
    // getMovieId(context, movieId) {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/api/v1/movies/${movieId}/`
    //   })
    //   .then((res) => {
    //     console.log(res.data)
    //     context.commit('GET_MOVIE', res.data)
    //   })
    //   .catch((err) => console.log(err))
    // },
    // // 한 영화의 전체 리뷰 조회
    // fetchReviews() {
    //   axios({
    //     method: 'get',
    //     url: `${API_URL}/api/v1/movies/${movieId}/reviews/`,
    //   })
    //   .then((res) => {
    //     console.log(res.data)
    //   })
    // },

    // 영화 조회
    updateMovies(context, Query) {
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
        console.log(res.data)
        context.commit('GET_MOVIES', res.data)
      })
      .catch((err) => console.log(err, Query))
    },
    
    // 
    
  },
}

export default movie