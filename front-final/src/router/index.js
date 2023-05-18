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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
