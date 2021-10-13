import Vue from 'vue'
import Vuex from 'vuex'

import ApiService from '@/services/api'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    data: null,
    profileId: null,
    filters: null,
    filterData: { basic: null, advanced: null },
  },
  mutations: {
    setData(state, data) {
      state.data = data
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

    getData({ commit }) {
      return ApiService.get('/map/').then((response) => {
        commit('setData', response)
      })
    },
  },
  modules: {},
  getters: {
    profile: (state) =>
      state.grid.profiles.find((e) => e.id == state.profileId),
  },
})
