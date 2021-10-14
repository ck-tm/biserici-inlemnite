<template>
  <div>
    <section
      v-for="(section, index) in filters.sections"
      :key="'section_' + filters.key + index"
    >
      <label class="label is-small is-sticky" v-if="section.title.length">
        {{ section.title }}
      </label>

      <FiltersAdvancedFilter
        v-for="filter in section.filters"
        :key="filter.key"
        v-model="model[filter.key]"
        :filter="filter"
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
    filters: null,
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
