import Vue from 'vue'
import VueRouter from 'vue-router'

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
        path: 'cont',
        component: () =>
          import(/* webpackChunkName: "account" */ '@/views/AccountBase.vue'),
        children: [
          {
            path: 'autentificare',
            name: 'AccountLogin',
            component: () =>
              import(
                /* webpackChunkName: "account" */ '@/views/AccountLogin.vue'
              ),
          },
          {
            path: 'inregistrare',
            name: 'AccountRegister',
            component: () =>
              import(
                /* webpackChunkName: "account" */ '@/views/AccountRegister.vue'
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

export default router
