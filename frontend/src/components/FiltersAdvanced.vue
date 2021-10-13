<template>
  <div>
    <label class="label is-small has-text-grey-light">Filtrare avansată</label>

    <b-tabs
      v-model="active.tab"
      animation="slide-prev slide-next"
      animateInitially
      vertical
    >
      <b-button
        icon-left="close"
        type="is-black"
        class="close"
        @click="toggleTab"
        v-if="active.tab"
      />

      <b-tab-item key="tab-null" :visible="false"></b-tab-item>

      <b-tab-item
        v-for="section in filterData"
        :key="'tab-' + section.key"
        class="is-full-height"
      >
        <template #header>
          <span v-text="section.title" />
          <b-icon icon="arrow-forward" />
        </template>

        <template #default>
          <div class="container-scroll">
            <h1 v-text="section.title" />

            <FiltersAdvancedSection
              v-model="filterModel[section.key]"
              :filterData="section"
              @input="update"
            />
          </div>
        </template>
      </b-tab-item>

      <div class="results" v-if="resultCount != null">
        <b-button type="is-primary" class="has-text-weight-bold">
          <span v-if="resultCount">
            Vezi {{ resultCount }}
            {{ resultCount > 1 ? 'rezultate' : 'rezultat' }}
          </span>
          <span v-else>Nu sunt rezultate</span>
        </b-button>
      </div>
    </b-tabs>
  </div>
</template>

<script>
import FiltersAdvancedSection from '@/components/FiltersAdvancedSection'
import ApiService from '@/services/api'

export default {
  name: 'FiltersAdvanced',
  components: { FiltersAdvancedSection },
  props: {
    filterData: Array,
  },
  data() {
    return {
      active: { tab: 0 },
      filterModel: {},
      resultCount: null,
    }
  },
  mounted() {},
  methods: {
    toggleTab() {
      if (this.active.tab) this.active.tab = 0
    },
    loadLocalities() {
      this.update()
    },
    updateFilter() {
      // if (this.filterModel) {}
    },
    update() {
      this.$store.commit('setFiltersAdvanced', this.filterModel)

      let postData = []

      Object.keys(this.filterModel).forEach((key) => {
        if (this.filterModel[key].length) {
          let cleanFilters = this.filterModel[key].filter(
            (e) => e != null && e.values.length
          )

          if (cleanFilters.length)
            postData.push({
              [key]: cleanFilters,
            })
        }
      })

      ApiService.post(
        '/filters/preview/',
        postData.length ? postData : undefined
      ).then((response) => {
        this.resultCount = postData.length ? response.count : null
      })
    },
  },
  computed: {},
}
</script>

<style lang="scss" scoped></style>
