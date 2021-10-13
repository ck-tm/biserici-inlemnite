<template>
  <div class="columns">
    <div class="column">
      <FiltersDropdown
        v-model="filterModel.judet"
        :options="filterData.judete"
        label="Județ"
        @input="loadLocalities"
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
        :options="filterData.conservare"
        label="Stare de conservare"
        @input="update"
      />
    </div>
    <div class="column">
      <FiltersDropdown
        v-model="filterModel.valoare"
        :options="filterData.valoare"
        label="Valoare patrimoniu"
        @input="update"
      />
    </div>
    <div class="column">
      <FiltersDropdown
        v-model="filterModel.prioritizare"
        :options="filterData.prioritizare"
        label="Prioritizare"
        @input="update"
      />
    </div>
  </div>
</template>

<script>
import FiltersDropdown from '@/components/FiltersDropdown'

export default {
  name: 'FiltersBasic',
  components: { FiltersDropdown },
  props: {
    filterData: Object,
  },
  data() {
    return {
      localities: this.filterData.localitati,
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
    loadLocalities() {
      this.localities = this.filterData.localitati.filter(
        (e) => e.judet == this.filterModel.judet.id
      )

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
