<template>
  <b-field v-bind="{ label }" customClass="is-small">
    <b-dropdown
      v-model="model"
      aria-role="menu"
      expanded
      scrollable
      v-bind="{
        // 'max-height': $mq == 'mobile' ? 400 : 580,
        'max-height': 400,
      }"
      @input="$emit('input', model)"
    >
      <template #trigger>
        <b-button
          :label="model ? options.find((e) => e.id == model[0]).value : 'Toate'"
          icon-right="arrow-down"
          size="is-small"
          expanded
        />
      </template>

      <b-dropdown-item
        v-for="item of options"
        :key="item.id"
        :value="[item.id]"
        aria-role="listitem"
      >
        {{ item.value }}
      </b-dropdown-item>
    </b-dropdown>
  </b-field>
</template>

<script>
export default {
  name: 'FiltersDropdown',
  props: {
    value: null,
    label: String,
    options: Array,
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
