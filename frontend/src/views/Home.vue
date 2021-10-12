<template>
  <div id="main-interface" class="is-full-height">
    <div class="filters-advanced">
      <FiltersAdvanced v-if="filters" :filters="filters.advanced" />
      <FiltersAdvanced :filters="dummyFilters" />
    </div>

    <div>
      <div class="filters-basic">
        <FiltersBasic v-if="filters" :filters="filters.basic" />
      </div>

      // MAP
    </div>

    <b-loading :is-full-page="false" v-model="filters" />
  </div>
</template>

<script>
import FiltersBasic from '@/components/FiltersBasic'
import FiltersAdvanced from '@/components/FiltersAdvanced'
// import ApiService from '@/services/api'
// import { mapState } from 'vuex'

export default {
  name: 'Home',
  components: { FiltersBasic, FiltersAdvanced },
  data() {
    return {
      filters: null,
      dummyFilters: [
        {
          title: 'Identificare',
          key: 'identificare',
          filters: [],
        },
        {
          title: 'Arhitectură',
          key: 'descriere',
          filters: [
            {
              title: 'Amplasament',
              key: 'amplasament',
              values: [
                {
                  id: 1,
                  nume: 'În cadrul așezării',
                },
              ],
            },
            {
              title: 'Topografie',
              key: 'topografie',
              values: [
                {
                  id: 2,
                  nume: 'La înălțime',
                },
              ],
            },
            {
              title: 'Relatia Cu Cimitirul',
              key: 'relatia_cu_cimitirul',
              values: [
                {
                  id: 1,
                  nume: 'În cadrul cimitirului',
                },
              ],
            },
          ],
        },
      ],
    }
  },
  computed: {},
  mounted() {
    // ApiService.get('/filters/').then((response) => {
    //   this.filters = response
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
