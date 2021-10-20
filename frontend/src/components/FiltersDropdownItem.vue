<template>
  <div></div>
</template>

<script>
export default {
  name: 'FiltersDropdownCircle',
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
