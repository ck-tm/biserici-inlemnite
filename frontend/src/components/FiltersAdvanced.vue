<template>
  <div>
    <label class="label is-small has-text-grey-light">Filtrare avansată</label>

    <b-tabs
      v-model="activeTab"
      animation="slide-prev slide-next"
      animateInitially
      vertical
    >
      <b-button
        icon-left="close"
        type="is-black"
        class="close"
        @click="toggleTab"
        v-if="activeTab"
      />

      <b-tab-item key="tab-null" :visible="false"></b-tab-item>

      <b-tab-item
        v-for="item in filters"
        :key="'tab-' + item.key"
        class="is-full-height"
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
      activeTab: 0,
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
      if (this.activeTab) this.activeTab = 0
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
