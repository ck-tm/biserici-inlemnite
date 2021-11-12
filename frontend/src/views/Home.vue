<template>
  <div class="container is-fullhd is-full-height">
    <FiltersAdvanced
      v-if="filters && $mq != 'mobile'"
      :filters="filters.advanced"
      @update="updateMap"
    />

    <div class="container-interface">
      <FiltersBasic
        v-if="filters && $mq != 'mobile'"
        :filters="filters.basic"
        @update="updateMap"
      />

      <div class="buttons buttons-toggle" v-if="this.$mq != 'mobile'">
        <b-button
          :type="active.mapList ? 'is-dark' : 'is-primary'"
          icon-left="pin"
          @click="active.mapList = false"
        >
          Hartă
        </b-button>
        <b-button
          :type="active.mapList ? 'is-primary' : 'is-dark'"
          icon-left="list"
          @click="active.mapList = true"
        >
          Listă
        </b-button>
      </div>

      <div class="container-map-profile">
        <MapList v-if="active.mapList" />
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
</template>

<script>
import FiltersBasic from '@/components/FiltersBasic'
import FiltersAdvanced from '@/components/FiltersAdvanced'
import Map from '@/components/Map'
import MapList from '@/components/MapList'
import ProfilePreview from '@/components/ProfilePreview'
import ProfileModal from '@/components/ProfileModal'

import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: {
    FiltersBasic,
    FiltersAdvanced,
    Map,
    MapList,
    ProfilePreview,
    ProfileModal,
  },
  data() {
    return {
      active: {
        profilePreview: false,
        profileModal: false,
        mapList: this.$mq != 'mobile',
      },
      viewType: 0,
    }
  },
  computed: {
    ...mapState(['filters']),
  },
  mounted() {
    if (!this.filters)
      this.$store.dispatch('getData', 'filters').then(() => {
        this.$store.dispatch('getMapData')
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
      if (this.$route.params.id)
        this.$router.push({ name: 'Home', params: { id: null } })

      this.$store.dispatch('getMapData')
    },
    // setViewType(type) {
    //   this.viewType = type
    // },
  },
  beforeRouteUpdate(to, from, next) {
    next()
    this.openProfilePreview()
  },
}
</script>

<style lang="scss" scoped>
.buttons-toggle {
  position: absolute;
  top: 130px;
  right: 16px;
  z-index: 37;
  background: $grey-dark;
  border: 1px solid $grey;
  border-radius: $radius;
  padding: 4px;

  /deep/.button {
    font-size: $size-7;
    height: 48px;
    width: 48px;
    flex-direction: column;
    align-items: center;
    margin-bottom: 0;

    &:not(:last-child):not(.is-fullwidth) {
      margin-right: 4px;
    }

    .icon {
      font-size: $size-3;

      &:first-child:not(:last-child) {
        margin: 0;
      }
    }
  }
}
</style>
