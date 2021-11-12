import Vue from 'vue'
import VueRouter from 'vue-router'
import TokenService from '@/services/storage'

import Base from '@/views/Base'
import Home from '@/views/Home'
import About from '@/views/About'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Base,
    children: [
      {
        path: 'despre',
        name: 'About',
        component: About,
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
        path: ':id?',
        name: 'Home',
        component: Home,
        meta: {},
      },
    ],
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
