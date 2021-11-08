import Vue from 'vue'
import Vuex from 'vuex'

import ApiService from '@/services/api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
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
