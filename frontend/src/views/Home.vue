<template>
  <div id="main-interface" class="is-full-height">
    <div id="filters-advanced" class="filters">
      <FiltersAdvanced v-if="filters" :filters="filters.advanced" />
    </div>

    <div class="container-interface">
      <div id="filters-basic" class="filters">
        <FiltersBasic v-if="filters" :filters="filters.basic" />
      </div>

      <div class="container-map-profile">
        <Map />
        <Profile
          :active="active.profileShort"
          @close="active.profileShort = false"
        />
      </div>
    </div>

    <b-loading :is-full-page="false" v-model="loading" />
  </div>
</template>

<script>
import FiltersBasic from '@/components/FiltersBasic'
import FiltersAdvanced from '@/components/FiltersAdvanced'
import Map from '@/components/Map'
import Profile from '@/components/Profile'

import ApiService from '@/services/api'
// import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: { FiltersBasic, FiltersAdvanced, Map, Profile },
  data() {
    return {
      filters: null,
      active: {
        profileShort: false,
      },
      loading: true,
    }
  },
  computed: {},
  mounted() {
    ApiService.get('/filters/')
      .then((response) => {
        this.filters = response
        this.loading = false

        this.$store.dispatch('getMapData')
      })
      .catch(() => {
        this.loading = false
      })
  },
  methods: {
    updateProfile() {
      this.active.profileShort = true
      this.$store.dispatch('getProfile', this.$route.params.id)
    },
  },
  beforeRouteUpdate(to, from, next) {
    next()
    this.updateProfile()
  },
}
</script>

<style lang="scss" scoped></style>
