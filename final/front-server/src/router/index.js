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
    path: '/movies',
    name: 'Movie',
    component: () => import('@/views/MoviePageView')
  },
  {
    path: '/movies/:id',
    name: 'MovieDetail',
    component: () => import('@/views/MovieDetailView')
  },
  {
    path: '/community',
    name: 'Community',
    component: () => import('@/views/CommunityPageView')
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
    path: '/profile/userid',
    name: 'Profile',
    component: () => import('@/views/ProfilePageView')
  },
  {
    path: '/lists',
    name: 'Lists',
    component: () => import('@/views/MovieListsView')
  },
  {
    path: '/reviews/:id',
    name: 'Reviews',
    component: () => import('@/views/ReviewDetailView')
  },

 
  // {
  //   path: '/create',
  //   name: 'CreateView',
  //   component: () => import('@/views/CreateView')
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
