<template>
  <div>
    <section
      v-for="(section, index) in filterData.sections"
      :key="'section_' + filterData.key + index"
    >
      <label class="label is-small is-sticky" v-if="section.title.length">
        {{ section.title }}
      </label>

      <FiltersAdvancedFilter
        v-for="filter in section.filters"
        :key="filter.key"
        v-model="model[filter.key]"
        :filterData="filter"
        @input="update(filter.key)"
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
    value: Object,
  },
  data() {
    return {
      model: this.computeValue(),
    }
  },
  mounted() {},
  methods: {
    computeValue() {
      return this.value ? { ...this.value } : {}
    },
    update(key) {
      if (!this.model[key].length) this.$delete(this.model, key)

      this.$emit('input', this.model)
    },
  },
  watch: {
    value() {
      this.model = this.computeValue()
    },
  },
}
</script>

<style lang="scss" scoped></style>
