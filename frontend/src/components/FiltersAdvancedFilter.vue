<template>
  <b-collapse animation="slide" @click="active = !active" :open="active">
    <template #trigger="props">
      <b-button
        icon-right="add"
        type="is-black"
        :active="props.open"
        :selected="model.length > 0"
        expanded
      >
        {{ filterData.title }}

        <span class="tag" v-if="model.length">
          ({{ model.length }})
        </span>
      </b-button>
    </template>

    <b-field>
      <b-checkbox
        v-for="(option, index) in filterData.values"
        :key="'option_' + filterData.key + (option.id || index)"
        v-model="model"
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
    value: Array,
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
      return this.value ? [...this.value] : []
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
