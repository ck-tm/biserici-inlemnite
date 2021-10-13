<template>
  <div id="main-interface" class="is-full-height">
    <div class="filters-advanced">
      <FiltersAdvanced v-if="filters" :filters="filters.advanced" />
    </div>

    <div>
      <div class="filters-basic">
        <FiltersBasic v-if="filters" :filters="filters.basic" />
      </div>

      // MAP
    </div>

    <b-loading :is-full-page="false" v-model="loading" />
  </div>
</template>

<script>
import FiltersBasic from '@/components/FiltersBasic'
import FiltersAdvanced from '@/components/FiltersAdvanced'
import { DummyFilters } from '@/services/utils'
// import ApiService from '@/services/api'
// import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: { FiltersBasic, FiltersAdvanced },
  data() {
    return {
      filters: DummyFilters,
      loading: true,
    }
  },
  computed: {},
  mounted() {
    // ApiService.get('/filters/').then((response) => {
    //   this.filters = response
    this.loading = false
    // })
  },
  methods: {
    // updateProfileId() {
    //   // console.log('[updateProfileId]', this.$route.params.id)
    //   this.$store.commit('setProfileId', this.$route.params.id)
    // },
  },
  // beforeRouteUpdate(to, from, next) {
  //   next()
  //   this.updateProfileId()
  // },
}
</script>

<style lang="scss" scoped></style>
