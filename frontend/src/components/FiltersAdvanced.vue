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
        v-for="section in filters"
        :key="'tab-' + section.key"
        class="is-full-height"
      >
        <template #header>
          <p>
            <span v-text="section.title" />
            <span class="tag" v-if="filterModel[section.key]">
              ({{ counters[section.key] }})
            </span>
          </p>
          <b-icon icon="arrow-forward" />
        </template>

        <template #default>
          <div class="container-scroll">
            <h1 v-text="section.title" />

            <FiltersAdvancedSection
              v-model="filterModel[section.key]"
              :filters="section"
              @input="update(section.key)"
            />
          </div>
        </template>
      </b-tab-item>

      <div class="results" v-if="resultCount != null">
        <b-button
          type="is-primary"
          class="has-text-weight-bold"
          :loading="loading"
          @click="applyFilters"
        >
          <span v-if="resultCount">
            Vezi {{ resultCount }}
            {{ resultCount > 1 ? 'rezultate' : 'rezultat' }}
          </span>
          <span v-else>Nu sunt rezultate</span>
        </b-button>
      </div>
    </b-tabs>

    <div class="filter-actions" v-if="filterTotalCount">
      <div class="results">
        <b>{{ filterTotalCount }}</b> filtre active
      </div>

      <b-button
        type="is-black"
        icon-left="trash"
        expanded
        @click="clearFilters"
      >
        Șterge filtrele
      </b-button>
    </div>
  </div>
</template>

<script>
import FiltersAdvancedSection from '@/components/FiltersAdvancedSection'
import ApiService from '@/services/api'
import { mapState } from 'vuex'

export default {
  name: 'FiltersAdvanced',
  components: { FiltersAdvancedSection },
  props: {
    filters: Array,
  },
  data() {
    return {
      active: { tab: 0 },
      filterModel: {},
      resultCount: null,
      counters: {},
      loading: false,
    }
  },
  mounted() {},
  methods: {
    toggleTab() {
      if (this.active.tab) this.active.tab = 0
    },
    clearFilters() {
      this.filterModel = {}
      this.counters = {}
      this.resultCount = null
    },
    update(key) {
      // remove empty keys / create non-existent
      if (!Object.keys(this.filterModel[key]).length) {
        this.$delete(this.filterModel, key)
        this.$delete(this.counters, key)
      } else
        this.$set(this.counters, key, Object.keys(this.filterModel[key]).length)

      this.loading = true

      ApiService.post('/filters/preview/', {
        advanced: this.filterModel,
        basic: this.filterBasic,
      }).then((response) => {
        this.resultCount = response.count
        this.loading = false
      })
    },
    applyFilters() {
      this.$store.commit('setFiltersAdvanced', this.filterModel)
      this.$store.dispatch('getMapData')

      this.active.tab = 0
    },
  },
  computed: {
    ...mapState({ filterBasic: (state) => state.filterData.basic }),
    filterTotalCount() {
      return Object.keys(this.counters).reduce(
        (sum, e) => sum + this.counters[e],
        0
      )
    },
  },
}
</script>

<style lang="scss" scoped></style>
