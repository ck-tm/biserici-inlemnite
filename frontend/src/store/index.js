import Vue from 'vue'
import Vuex from 'vuex'

import ApiService from '@/services/api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    profile: {
      id: null,
      data: null,
    },
    filters: null,
    filterData: { basic: {}, advanced: {} },
    mapData: null,
  },
  mutations: {
    setMapData(state, data) {
      state.mapData = data
    },
    setProfileId(state, data) {
      state.profile.id = data
    },
    setFilters(state, data) {
      state.filters = data
    },
    setFiltersBasic(state, data) {
      state.filterData.basic = data
    },
    setFiltersAdvanced(state, data) {
      state.filterData.advanced = data
    },
  },
  actions: {
    getFilters({ commit }) {
      return ApiService.get('/filters/').then((response) => {
        commit('setFilters', response)
      })
    },

    getMapData({ commit, state }) {
      return Object.keys(state.filterData.basic).length ||
        Object.keys(state.filterData.advanced).length
        ? ApiService.post('/map/filter/', state.filterData).then((response) => {
            commit('setMapData', response)
          })
        : ApiService.get('/map/').then((response) => {
            commit('setMapData', response)
          })
    },
  },
  modules: {},
  getters: {
    profilePreview: (state) =>
      state.mapData && state.profile.id
        ? state.mapData.find((e) => e.id == state.profile.id)
        : null,
    filterValue: (state) => (filter, value) =>
      state.filters
        ? state.filters.basic[filter].find((e) => e.id == value).value
        : null,
  },
})
