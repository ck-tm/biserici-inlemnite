<template>
  <div id="filters-basic" class="filters">
    <div class="columns">
      <div class="column">
        <FiltersDropdown
          v-model="filterModel.judet"
          :options="filters.judet"
          label="Județ"
          @input="filterLocalities"
        />
      </div>
      <div class="column">
        <FiltersDropdown
          v-model="filterModel.localitate"
          :options="localities"
          label="Localitate"
          @input="update"
        />
      </div>
      <div class="column">
        <FiltersDropdown
          v-model="filterModel.conservare"
          :options="filters.conservare"
          label="Stare de conservare"
          @input="update"
        />
      </div>
      <div class="column">
        <FiltersDropdown
          v-model="filterModel.valoare"
          :options="filters.valoare"
          label="Valoare patrimoniu"
          @input="update"
        />
      </div>
      <div class="column">
        <FiltersDropdown
          v-model="filterModel.prioritizare"
          :options="filters.prioritizare"
          label="Prioritizare"
          @input="update"
        />
      </div>
    </div>
  </div>
</template>

<script>
import FiltersDropdown from '@/components/FiltersDropdown'

export default {
  name: 'FiltersBasic',
  components: { FiltersDropdown },
  props: {
    filters: Object,
  },
  data() {
    return {
      localities: this.filters.localitate,
      filterModel: {
        // judet: [],
        // localitate: [],
        // conservare: [],
        // valoare: [],
        // prioritizare: [],
      },
    }
  },
  mounted() {},
  methods: {
    filterLocalities() {
      this.localities = this.filters.localitate.filter(
        (e) => e.judet == this.filterModel.judet[0]
      )

      this.update()
    },
    update() {
      this.$store.commit('setFiltersBasic', this.filterModel)
      this.$store.dispatch('getMapData')
    },
  },
  computed: {},
}
</script>

<style lang="scss" scoped>
#filters-basic {
  flex: none;
  padding: 22px 32px;
  border-bottom: 1px solid $grey;
  z-index: 38;

  .columns {
    width: 100%;
    max-width: 1100px;
    align-items: flex-end;
  }
}
</style>
