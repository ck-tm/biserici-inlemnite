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
        {{ filter.title }}

        <span class="tag is-black" v-if="model.length">
          ({{ model.length }})
        </span>
      </b-button>
    </template>

    <b-field>
      <b-checkbox
        v-for="(option, index) in filter.values"
        :key="'option_' + filter.key + index"
        v-model="model"
        :native-value="option.id"
        @input="update"
      >
        <template v-if="filter.type == 'poza'">
          <img
            :src="'https://biserici-inlemnite.ro' + option.url"
            :alt="option.alt"
          />
        </template>
        <template v-else>
          {{ option.nume | formatFieldValue }}
        </template>
      </b-checkbox>
    </b-field>
  </b-collapse>
</template>

<script>
export default {
  name: 'FiltersAdvancedFilter',
  props: {
    value: Array,
    filter: Object,
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
