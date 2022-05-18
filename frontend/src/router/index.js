import Vue from 'vue'
import VueRouter from 'vue-router'
import TokenService from '@/services/storage'

import Base from '@/views/Base'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Base,
    children: [
      {
        path: 'about',
        name: 'About',
        component: () =>
          import(/* webpackChunkName: "account" */ '@/views/About.vue'),
      },
      {
        path: 'account',
        component: () =>
          import(/* webpackChunkName: "account" */ '@/views/AccountBase.vue'),
        meta: {
          anonymousOnly: true,
        },
        children: [
          {
            path: 'login',
            name: 'AccountLogin',
            component: () =>
              import(
                /* webpackChunkName: "account" */ '@/views/AccountLogin.vue'
              ),
          },
          {
            path: 'register',
            name: 'AccountRegister',
            component: () =>
              import(
                /* webpackChunkName: "account" */ '@/views/AccountRegister.vue'
              ),
          },
          {
            path: 'activate/:uid/:token',
            name: 'AccountActivate',
            component: () =>
              import(
                /* webpackChunkName: "account" */ '@/views/AccountActivate.vue'
              ),
          },
        ],
      },
      {
        path: '/profile/:id',
        name: 'Profile',
        component: () =>
          import(/* webpackChunkName: "home" */ '@/views/Profile.vue'),
      },
      {
        path: ':id?',
        name: 'Home',
        component: () =>
          import(/* webpackChunkName: "home" */ '@/views/Home.vue'),
      },
    ],
  },
  {
    path: '/profile-print/:id',
    name: 'ProfilePrint',
    component: () =>
      import(/* webpackChunkName: "home" */ '@/views/ProfilePrint.vue'),
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

router.beforeEach((to, from, next) => {
  const anonymousOnly = to.matched.some((record) => record.meta.anonymousOnly)
  const isLoggedIn = !!TokenService.getToken()

  if (anonymousOnly && isLoggedIn) {
    return next('/')
  }

  next()
})

export default router
