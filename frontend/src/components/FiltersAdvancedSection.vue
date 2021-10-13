<template>
  <div>
    <section v-for="(filter, index) in filterData.filters" :key="filter.key">
      <label class="label is-small is-hidden">
        {{ filter.title }}
      </label>

      <FiltersAdvancedFilter
        v-model="model[index]"
        :filterData="filter"
        @input="update"
      />
    </section>
  </div>
</template>

<script>
import FiltersAdvancedFilter from '@/components/FiltersAdvancedFilter'
export default {
  name: 'FiltersAdvancedSection',
  components: { FiltersAdvancedFilter },
  props: {
    filterData: null,
    value: Array,
  },
  data() {
    return {
      model: this.computeValue(),
      active: {},
    }
  },
  mounted() {},
  methods: {
    computeValue() {
      return this.value ? [...this.value] : []
    },
    update() {
      // console.log('[update]', event, key, this.model)
      this.$emit('input', this.model)
    },
    toggleFilter(key) {
      this.$set(this.active, key, true)
    },
    submit() {},
  },
  watch: {
    value() {
      this.model = this.computeValue()
    },
  },
}
</script>

<style lang="scss" scoped></style>
