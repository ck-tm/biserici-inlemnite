import Vue from 'vue'
import VueRouter from 'vue-router'

import Base from '../views/Base.vue'
import Home from '../views/Home.vue'
// import About from '../views/About.vue'
// import Register from '../views/Register.vue'
// import Resources from '../views/Resources.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    component: Base,
    children: [
      // {
      //   path: '/about',
      //   name: 'About',
      //   component: About,
      // },
      // {
      //   path: '/register/:success?',
      //   name: 'Register',
      //   component: Register,
      // },
      // {
      //   path: '/resources',
      //   name: 'Resources',
      //   component: Resources,
      // },
      {
        path: '/:id?',
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
