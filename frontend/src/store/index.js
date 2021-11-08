import Vue from 'vue'
import Vuex from 'vuex'
import router from '@/router'

import ApiService from '@/services/api'
import UserService from '@/services/user'
import TokenService from '@/services/storage'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: TokenService.getToken(),
    about: null,
    profile: {
      id: null,
      data: null,
    },
    filters: null,
    filterData: { basic: {}, advanced: {} },
    mapData: null,
    loading: null,
  },
  mutations: {
    login(state, token) {
      state.token = token
    },
    logout(state) {
      state.token = null
    },
    setMapData(state, data) {
      state.mapData = data
    },
    setProfileId(state, data) {
      state.profile.id = data
    },
    setLoading(state, data) {
      state.loading = data
    },
    setData(state, { data, name }) {
      state[name] = data
    },
    setFiltersBasic(state, data) {
      state.filterData.basic = data
    },
    setFiltersAdvanced(state, data) {
      state.filterData.advanced = data
    },
  },
  actions: {
    login({ commit }, { username, password }) {
      return UserService.login(username, password)
        .then((response) => {
          commit('login', response)

          router.replace(router.history.current.query.redirect || '/')
        })
        .catch(() => {})
    },

    logout({ commit }) {
      UserService.logout()
      commit('logout')

      router.push('/')
    },
    getData({ commit }, name) {
      commit('setLoading', true)

      return ApiService.get(`/${name}/`)
        .then((response) => {
          commit('setData', { data: response, name })
          commit('setLoading', false)
        })
        .catch(() => {
          commit('setLoading', false)
        })
    },

    getMapData({ commit, state }) {
      const request =
        Object.keys(state.filterData.basic).length ||
        Object.keys(state.filterData.advanced).length
          ? ApiService.post('/map/filter/', state.filterData)
          : ApiService.get('/map/')

      commit('setLoading', true)

      return request
        .then((response) => {
          commit('setMapData', response)
          commit('setLoading', false)
        })
        .catch(() => {
          commit('setLoading', false)
        })
    },
  },
  modules: {},
  getters: {
    profilePreview: (state) =>
      state.mapData && state.profile.id
        ? state.mapData.find((e) => e.id == state.profile.id)
        : null,
    filterValue: (state) => (filter, value) => {
      if (state.filters && value) {
        const result = state.filters.basic[filter].find((e) => e.id == value)
        return result && result.value
      }

      return null
    },
  },
})
