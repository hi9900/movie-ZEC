import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

// 홈 -> 홈 새로고침
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(() => {
    return window.location.reload()
  })
}

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
    name: 'SignUp',
    component: () => import('@/views/SignUpView')
  },

  {
    path: '/login',
    name: 'LogIn',
    component: () => import('@/views/LogInView')
  },
  {
    path: '/update',
    name: 'Update',
    component: () => import('@/views/UpdateView')
  },
  {
    path: '/profile/:username',
    name: 'Profile',
    component: () => import('@/views/ProfilePageView')
  },
  {
    path: "/profile/:username/followers",
    name: "FollowersList",
    component: () => import("@/views/FollowersListView"),
  },
  {
    path: "/profile/:username/following",
    name: "FollowingList",
    component: () => import("@/views/FollowingListView"),
  },
  {
    path: '/lists',
    name: 'Lists',
    component: () => import('@/views/MovieListsView')
  },
  {
    path: '/lists/:id',
    name: 'ListsDetail',
    component: () => import('@/views/ListsDirectorView')
  },
  {
    path: '/reviews/:reviewId',
    name: 'ReviewDetail',
    component: () => import('@/views/ReviewDetailView')
  },


 
  // {
  //   path: '/create',
  //   name: 'CreateView',
  //   component: () => import('@/views/CreateView')
  // },

]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
