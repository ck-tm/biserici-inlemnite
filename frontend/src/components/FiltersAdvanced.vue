<template>
  <div>
    <label class="label is-small has-text-grey-light">Filtrare avansată</label>

    <b-tabs v-model="activeTab" vertical>
      <b-tab-item
        v-for="item in filters"
        :key="'filter-' + item.key"
        class="is-full-height"
        @click="toggleTab"
      >
        <template #header>
          <span v-text="item.title" />
          <b-icon icon="arrow-forward" />
        </template>

        <h1 v-text="item.title" />
      </b-tab-item>
    </b-tabs>
  </div>
</template>

<script>
// import { FiltersDropdown } from '@/components/FiltersDropdown'

export default {
  name: 'FiltersAdvanced',
  // components: { FiltersDropdown },
  props: {
    filters: Array,
  },
  data() {
    return {
      activeTab: null,
      filterModel: {
        judet: null,
        localitate: null,
        conservare: null,
        valoare: null,
        prioritizare: null,
      },
    }
  },
  mounted() {},
  methods: {
    toggleTab() {
      if (this.activeTab) this.activeTab = null
    },
    loadLocalities() {
      this.update()
    },
    update() {
      this.$store.commit('setFiltersBasic', this.filterModel)
    },
  },
  computed: {},
}
</script>

<style lang="scss" scoped></style>
