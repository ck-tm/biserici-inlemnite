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
              :filterData="section"
              @input="update(section.key)"
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
// import ApiService from '@/services/api'

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
      counters: {},
    }
  },
  mounted() {},
  methods: {
    toggleTab() {
      if (this.active.tab) this.active.tab = 0
    },
    clearFilters() {
      this.filterModel = {}
    },
    update(key) {
      if (!Object.keys(this.filterModel[key]).length) {
        this.$delete(this.filterModel, key)
        this.$delete(this.counters, key)
      } else {
        this.$set(this.counters, key, Object.keys(this.filterModel[key]).length)
      }

      this.$store.commit('setFiltersAdvanced', this.filterModel)
    },
  },
  computed: {
    filterTotalCount() {
      return Object.keys(this.counters).reduce((sum, e) => sum + this.counters[e], 0)
    },
  },
}
</script>

<style lang="scss" scoped></style>
