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
  // 영화
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
  // 리뷰
  {
    path: '/reviews/:reviewId',
    name: 'ReviewDetail',
    component: () => import('@/views/ReviewDetailView')
  },

  // 프로필
  {
    path: '/profile/:username',
    component: () => import('@/views/ProfilePageView'),
    children: [
      {
        path: 'reviews',
        name: 'Profile',
        component: () => import('@/views/ProfileReviewView')
      },
      {
        path: 'followers',
        name: 'FollowersList',
        component: () => import('@/views/FollowersListView')
      },
      {
        path: 'followings',
        name: 'FollowingList',
        component: () => import('@/views/FollowingsListView')
      }
    ]
  },

  // account
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

  // 리스트
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
    path: '/community',
    name: 'Community',
    component: () => import('@/views/CommunityPageView')
  },
  {
    path: '/article',
    name: 'Article',
    redirect: '/article/list',
    component: () => import('@/views/ArticleView'),
    children: [
      {
        path: 'list',
        name: 'ArticleList',
        component: () => import('@/components/article/ArticleList')
      },
      {
        path: 'detail',
        name: 'ArticleDetail',
        component: () => import('@/components/article/ArticleDetail')
      },
      {
        path: 'create',
        name: 'ArticleCreate',
        component: () => import('@/components/article/ArticleCreate')
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    // scrollBehavior 메서드 추가
    return {x: 0, y: 0}
  }
})

export default router
