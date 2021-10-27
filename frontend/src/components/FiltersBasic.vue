<template>
  <div id="filters-basic" class="filters">
    <div class="columns">
      <div class="column">
        <FiltersDropdown
          v-model="filterModel.judet"
          :options="filters.judet"
          index="judet"
          label="Județ"
          @input="filterLocalities"
        />
      </div>
      <div class="column">
        <FiltersDropdown
          v-model="filterModel.localitate"
          :options="localities"
          index="localitate"
          label="Localitate"
          @input="update"
        />
      </div>
      <div class="column">
        <FiltersDropdown
          v-model="filterModel.conservare"
          :options="filters.conservare"
          index="conservare"
          label="Stare de conservare"
          @input="update"
        />
      </div>
      <div class="column">
        <FiltersDropdown
          v-model="filterModel.valoare"
          :options="filters.valoare"
          index="valoare"
          label="Valoare patrimoniu"
          @input="update"
        />
      </div>
      <div class="column">
        <FiltersDropdown
          v-model="filterModel.prioritizare"
          :options="filters.prioritizare"
          index="prioritizare"
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
      filterModel: {},
    }
  },
  mounted() {},
  methods: {
    filterLocalities() {
      if (this.filterModel.judet[0])
        this.localities = this.filters.localitate.filter(
          (e) => e.judet == this.filterModel.judet[0]
        )
      else this.localities = this.filters.localitate

      this.update()
    },
    update() {
      Object.keys(this.filterModel).forEach((key) => {
        if (!this.filterModel[key].length) this.$delete(this.filterModel, key)
      })

      this.$store.commit('setFiltersBasic', this.filterModel)
      this.$emit('update')
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
    align-items: flex-end;
  }
}
</style>
