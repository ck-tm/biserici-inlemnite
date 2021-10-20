<template>
  <div id="main-interface" class="is-full-height">
    <div class="container is-fullhd">
      <FiltersAdvanced
        v-if="filters"
        :filters="filters.advanced"
        @update="updateMap"
      />

      <div class="container-interface">
        <FiltersBasic
          v-if="filters"
          :filters="filters.basic"
          @update="updateMap"
        />

        <div class="container-map-profile">
          <Map />

          <ProfilePreview
            :active="active.profilePreview"
            @close="active.profilePreview = false"
            @openProfileModal="openProfileModal"
          />
        </div>

        <ProfileModal
          :active="active.profileModal"
          @close="active.profileModal = false"
        />
      </div>
    </div>

    <b-loading v-model="loading" />
  </div>
</template>

<script>
import FiltersBasic from '@/components/FiltersBasic'
import FiltersAdvanced from '@/components/FiltersAdvanced'
import Map from '@/components/Map'
import ProfilePreview from '@/components/ProfilePreview'
import ProfileModal from '@/components/ProfileModal'

import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    FiltersBasic,
    FiltersAdvanced,
    Map,
    ProfilePreview,
    ProfileModal,
  },
  data() {
    return {
      active: {
        profilePreview: false,
        profileModal: false,
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

    if (this.$route.params.id) this.openProfilePreview()
  },
  methods: {
    openProfileModal() {
      this.active.profileModal = true
    },
    openProfilePreview() {
      this.$store.commit('setProfileId', this.$route.params.id)
    },
    updateMap() {
      this.loading = true
      this.$router.push({ name: 'Home', params: { id: null } })

      this.$store
        .dispatch('getMapData')
        .then(() => {
          this.loading = false
        })
        .catch(() => {
          this.loading = false
        })
    },
  },
  beforeRouteUpdate(to, from, next) {
    next()
    this.openProfilePreview()
  },
}
</script>

<style lang="scss" scoped></style>
