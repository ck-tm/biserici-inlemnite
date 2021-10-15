<template>
  <div>
    <b-dropdown-item
        v-for="item of options"
        :key="item.id"
        :value="[item.id]"
        aria-role="listitem"
      >
        {{ item.value }}
      </b-dropdown-item>
  </div>
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
