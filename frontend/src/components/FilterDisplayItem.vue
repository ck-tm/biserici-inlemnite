<template>
  <div class="filter-item">
    <div
      class="label is-small"
      v-text="basicFilters[index].label"
      v-if="hasLabel"
    />

    <div class="item" :class="{ 'is-flex': isMultiline }">
      <div class="tag bullet" :class="classTag" v-text="value" />

      <p
        class="caption"
        v-if="hasCaption"
        v-text="
          basicFilters[index].options.find((e) =>
            e.interval
              ? value >= e.interval[0] && value <= e.interval[1]
              : value == e.id
          ).value
        "
      />
    </div>
  </div>
</template>

<script>
import { BasicFilters } from '@/services/utils'

export default {
  name: 'FilterDisplayItem',
  props: {
    value: null,
    index: String,
    isLarge: Boolean,
    isMultiline: Boolean,
    hasLabel: { type: Boolean, default: true },
    hasCaption: { type: Boolean, default: true },
  },
  data() {
    return {
      basicFilters: BasicFilters,
    }
  },
  mounted() {},
  methods: {},
  computed: {
    classTag() {
      return {
        'is-large': this.isLarge,
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.filter-item {
  .label {
    margin-bottom: 16px;
  }

  .tag {
    margin-right: 16px;
  }

  .caption {
    font-size: $size-7;
  }

  .item {
    align-items: center;

    &:not(.is-flex) {
      .tag {
        margin-bottom: 8px;
      }
    }
  }
}
</style>
