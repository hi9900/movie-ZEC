import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

const list = {
  namespaced: true,
  state: {
    directorMovies: [],
    genreMovies: [],
    randomMovies: [],
    actorMovies: [],
    movies: [],
    movielists: [],
  },
  getters: {
  },  
  mutations: {
    GET_RANDOM(state, movies){
      state.directorMovies = movies.director_movies
      state.genreMovies = movies.genre_movies
      state.actorMovies = movies.actor_movies
    },
    // GET_DIRECTOR(state, movies) {
    //   state.directorMovies = movies
    // },
    // GET_GENRE(state, movies) {
    //   state.genreMovies = movies
    // },
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    GET_LISTS(state, movies){
      state.movielists = movies
    }
  },
  actions: {
    getMovie(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/random/`
      })
      .then ((res) => {
        console.log(res.data)
        context.commit('GET_RANDOM', res.data)
      })
      .catch((err) => console.log(err))
      // await axios
      // .all([
      //   // axios.get(`${API_URL}/api/v1/movies/directors/random/`), 
      //   axios.get(`${API_URL}/api/v1/movies/genres/random/`)
      // ])
      // .then(
      //   axios.spread((res2) => {
      //   console.log(res2)
      //   // context.commit('GET_DIRECTOR', res1.data)
      //   context.commit('GET_GENRE', res2.data)
      // })
      // )
      // .catch((err) => console.log(err))
    },

    getDirector(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/directors/random/`,
      })
      .then((res) => {
        // console.log(res.data)
        context.commit('GET_DIRECTOR', res.data)
      })
      .catch((err) => console.log(err))
    },
    getDirectorId(context, directorId) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/movies/directors/${directorId}/`,
      })
      .then((res) => {
        console.log(res.data)
        context.commit('GET_MOVIES', res.data)
      })
      .catch((err) => console.log(err))
    },
    getGenre(context) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movies/genres/random/`,
    })
    .then((res) => {
      console.log(res.data)
      context.commit('GET_GENRE', res.data)
    })
    .catch((err) => console.log(err))
  },
  getLists(context) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/movie_lists/`,
    })
    .then((res) => {
      console.log(res.data)
      context.commit('GET_LISTS', res.data)
    })
    .catch((err) => console.log(err))
  },
  },
}

export default list