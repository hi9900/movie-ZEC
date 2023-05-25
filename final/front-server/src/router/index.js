// router/index.js
import Vue from 'vue'
import VueRouter from 'vue-router'
import store from '@/store/index'

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
    component: () => import('@/views/MoviePageView')
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
    path: '/lists/derector/:id',
    name: 'ListsDerector',
    component: () => import('@/views/ListsDirectorView')
  },
  {
    path: '/lists/Genre/:id',
    name: 'ListsGenre',
    component: () => import('@/views/ListsGenreView')
  },
  {
    path: '/lists/actor/:id',
    name: 'ListsActor',
    component: () => import('@/views/ListsActorView')
  },


  // 게시판
  {
    path: '/article',
    name: 'Article',
    redirect: '/article/list',
    component: () => import('@/views/ArticleView'),
    props: true,
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
      },
      {
        path: '/create-comment/:articleId',
        name: 'CreateComment',
        component: () => import('@/components/article/CommentCreate')
      },
      {
        path: '/:articleId',
        name: 'ArticleUpdate',
        component: () => import('@/components/article/ArticleUpdate')
      },
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior() {
    // scrollBehavior 메서드 추가
    return { x: 0, y: 0 }
  }
})

router.beforeEach((to, from, next) => {
  // CODE HERE
  //  console.log('to', to)
  //  console.log('from', from)
  //  console.log('next', next)

  // 로그인 여부
  // const isLoggedIn = false
  const isLogin = store.getters['account/isLogin']

  // 로그인이 필요한 페이지 지정
  const authPages = [
    'MovieDetail',
    'ReviewDetail',
    'Profile',
    'FollowersList',
    'FollowingList',
    'Update',
    'ListsDetail',
    'Lists',
    'Update'
  ]
  // 앞으로 이동할 페이지(to)가 로그인이 필요한 페이지인지 확인
  const isAuthRequired = authPages.includes(to.name)

  if (isAuthRequired && !isLogin) {
    console.log('Login')
    // next({name: 'LogIn'})
    alert('로그인이 필요한 페이지입니다.')
  } else {
    console.log('to')
    next()
  }
})

export default router
