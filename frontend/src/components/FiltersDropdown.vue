<template>
  <v-field label="">
    <b-dropdown
      v-model="model"
      aria-role="menu"
      expanded
      scrollable
      v-bind="{
        'max-height': $mq == 'mobile' ? 400 : 580,
      }"
      @input="$emit('input', model)"
    >
      <template #trigger>
        <b-button
          :label="model ? model.value : 'Toate'"
          icon-right="arrow-down"
        />
      </template>

      <b-dropdown-item
        v-for="item of filters"
        :key="item.id"
        :value="item"
        aria-role="listitem"
      >
        {{ item.value }}
      </b-dropdown-item>
    </b-dropdown>
  </v-field>
</template>

<script>
export default {
  name: 'FiltersDropdown',
  props: {
    value: null,
    label: String,
    filters: Array,
  },
  data() {
    return {
      model: this.value,
    }
  },
  mounted() {},
  methods: {},
  watch: {
    value(val) {
      this.model = val
    },
  },
}
</script>

<style lang="scss" scoped></style>
