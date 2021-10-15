<template>
  <div id="main-interface" class="is-full-height">
    <FiltersAdvanced v-if="filters" :filters="filters.advanced" />

    <div class="container-interface">
      <FiltersBasic v-if="filters" :filters="filters.basic" />

      <div class="container-map-profile">
        <Map />

        <ProfilePreview
          :active="active.profilePreview"
          @close="active.profilePreview = false"
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
import ProfilePreview from '@/components/ProfilePreview'

import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: { FiltersBasic, FiltersAdvanced, Map, ProfilePreview },
  data() {
    return {
      active: {
        profilePreview: false,
      },
      loading: true,
    }
  },
  computed: {
    ...mapState(['filters']),
  },
  mounted() {
    this.$store
      .dispatch('getFilters')
      .then(() => {
        this.loading = false
        this.$store.dispatch('getMapData')
      })
      .catch(() => {
        this.loading = false
      })
  },
  methods: {
    updateProfile() {
      this.active.profilePreview = true
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
