<template>
  <div class="columns">
    <div class="column">
      <FiltersDropdown
        v-model="filterModel.judet"
        :options="filters.judete"
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
        :options="filters.localitati"
        label="Localitate"
        @input="update"
      />
    </div>
    <div class="column">
      <FiltersDropdown
        v-model="filterModel.localitate"
        :options="filters.localitati"
        label="Localitate"
        @input="update"
      />
    </div>
    <div class="column">
      <FiltersDropdown
        v-model="filterModel.localitate"
        :options="filters.localitati"
        label="Localitate"
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
    filters: Object,
  },
  data() {
    return {
      localities: this.filters.localitati,
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
      this.localities = this.filters.localitati.filter(
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
