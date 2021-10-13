<template>
  <div class="columns is-gapless">
    <div class="column">
      <FiltersDropdown
        v-model="filterModel.judet"
        :filters="filters.basic.judete"
        :label="Județ"
        @input="loadLocalities"
      />

      <FiltersDropdown
        v-model="filterModel.localitate"
        :filters="filters.basic.localitati"
        :label="Localitate"
        @input="update"
      />
    </div>
  </div>
</template>

<script>
// import { EntityIcons } from '@/services/utils'
import { FiltersDropdown } from '@/components/FiltersDropdown'

export default {
  name: 'FiltersBasic',
  components: { FiltersDropdown },
  props: {
    filters: Object,
  },
  data() {
    return {
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
