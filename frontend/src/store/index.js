import Vue from 'vue'
import Vuex from 'vuex'

import ApiService from '@/services/api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    profileId: null,
    filters: null,
    filterData: { basic: {}, advanced: {} },
    mapData: null,
  },
  mutations: {
    setMapData(state, data) {
      state.mapData = data
    },
    setProfileId(state, data) {
      state.profileId = data
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
        ? ApiService.post('/map/', state.filterData).then((response) => {
            commit('setMapData', response)
          })
        : ApiService.get('/map/').then((response) => {
            commit('setMapData', response)
          })
    },
  },
  modules: {},
  getters: {
    profile: (state) => state.mapData.find((e) => e.id == state.profileId),
  },
})
