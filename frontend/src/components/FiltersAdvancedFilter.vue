<template>
  <b-collapse animation="slide" @click="active = !active">
    <template #trigger>
      <b-button
        icon-right="add"
        :label="
          filterData.title + (model.values ? ` (${model.values.length})` : '')
        "
        type="is-black"
        expanded
      />
    </template>

    <b-field>
      <b-checkbox
        v-for="option in filterData.values"
        :key="'option_' + filterData.key + option.id"
        v-model="model.values"
        :native-value="option.id"
        @input="update"
      >
        {{ option.nume }}
      </b-checkbox>
    </b-field>
  </b-collapse>
</template>

<script>
export default {
  name: 'FiltersAdvancedFilter',
  props: {
    value: Object,
    filterData: Object,
  },
  data() {
    return {
      model: this.computeValue(),
      active: false,
    }
  },
  mounted() {},
  methods: {
    computeValue() {
      return this.value
        ? Object.assign({}, this.value)
        : {
            key: this.filterData.key,
            values: [],
          }
    },
    update() {
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
