import Vue from 'vue'

import App from './App.vue'
import router from './router'
import store from './store'
import i18n from './vue-i18n'

import ApiService from './services/api'

import VueMeta from 'vue-meta'
import VueScrollTo from 'vue-scrollto'
import VueMq from 'vue-mq'
import './libs/buefy'
import './libs/form-validation'

import './components/globals'
import './services/filters'

// Styles
import './assets/style/base.scss'

ApiService.init(process.env.VUE_APP_ROOT_API)
ApiService.setHeader()

Vue.use(VueMeta)
Vue.use(VueScrollTo)
Vue.use(VueMq, {
  breakpoints: {
    mobile: 1080,
    desktop: Infinity,
  },
})
Vue.config.productionTip = false

new Vue({
  i18n,
  router,
  store,
  render: (h) => h(App),
}).$mount('#app')
