import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/views/HomePageView')
  },
  {
    path: '/movie',
    name: 'Movie',
    component: () => import('@/views/MoviePageView')
  },
  {
    path: '/community',
    name: 'Community',
    component: () => import('@/views/CommunityPageView')
  },
  {
    // path: '/movie/:id',
    path: '/movie/id',
    name: 'MovieDetail',
    component: () => import('@/views/MovieDetailView')
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: () => import('@/views/SignUpView')
  },

  {
    path: '/login',
    name: 'LogInView',
    component: () => import('@/views/LogInView')
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('@/views/ProfilePageView')
  }

  // {
  //   path: '/article',
  //   name: 'ArticleView',
  //   component: () => import('@/views/ArticleView')
  // },
 
  // {
  //   path: '/create',
  //   name: 'CreateView',
  //   component: () => import('@/views/CreateView')
  // },

  // {
  //   path: '/:id',
  //   name: 'DetailView',
  //   component: () => import('@/views/DetailView'),
  // },
]

// const scrollBehavior = function (to, from, savedPosition) {
//   if (savedPosition) {
//     return savedPosition
//   } else {
//     return { x: 0, y: 0 }
//   }
// }

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  
  // scrollBehavior
})

export default router
