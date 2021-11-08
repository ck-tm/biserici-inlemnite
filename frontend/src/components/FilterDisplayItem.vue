<template>
  <div
    class="filter-item"
    :class="{ [`is-${index}`]: true, ...classTag }"
    v-if="activeOption"
  >
    <div
      class="label is-small"
      v-text="basicFilters[index].label"
      v-if="hasLabel"
    />

    <div class="item" :class="{ 'is-flex': !isMultiline }">
      <div class="tag" v-text="displayValue" :style="tagStyle" />
      <p class="caption" v-if="hasCaption" v-text="activeOption.value" />
    </div>
  </div>
</template>

<script>
import { Colors, BasicFilters } from '@/services/utils'

export default {
  name: 'FilterDisplayItem',
  props: {
    value: null,
    index: String,
    size: String,
    isMultiline: { type: Boolean, default: false },
    hasLabel: { type: Boolean, default: true },
    hasCaption: { type: Boolean, default: true },
    hasSizeVariation: { type: Boolean, default: false },
    useInterval: { type: Boolean, default: true },
  },
  data() {
    return {
      basicFilters: BasicFilters,
    }
  },
  mounted() {},
  methods: {
    compFunc(e) {
      return e.interval && this.useInterval
        ? this.value >= e.interval[0] && this.value <= e.interval[1]
        : Math.round(this.value) == e.id
    },
  },
  computed: {
    displayValue() {
      return this.value
        ? Math.round(this.value * 10) / 10
        : BasicFilters[this.index].default.id
    },
    activeOption() {
      return (
        BasicFilters[this.index].options.find((e) => this.compFunc(e)) ||
        BasicFilters[this.index].default
      )
    },
    classTag() {
      return {
        [this.size]: true,
      }
    },
    tagStyle() {
      const i = BasicFilters[this.index].options.findIndex((e) =>
        this.compFunc(e)
      )

      if (i == -1) {
        return {
          background: BasicFilters[this.index].default.background,
        }
      }

      if (Colors[this.index])
        return {
          'background-color': Colors[this.index][i],
          'border-color': Colors[this.index][i],
          color: '#000000',
        }

      if (this.activeOption && this.activeOption.size) {
        if (this.hasSizeVariation)
          return {
            'background-color': '#CCCCCC',
            'border-color': '#CCCCCC',
            'font-size': 0,
            width: this.activeOption.size + 'px',
            height: this.activeOption.size + 'px',
            'margin-left': (24 - this.activeOption.size) / 2 + 'px',
            'margin-right': 12 + (24 - this.activeOption.size) / 2 + 'px',
          }
        else return { 'background-color': '#FFFFFF', color: '#000000' }
      }

      return {
        // 'border-color': '#FFFFFF',
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
    width: 32px;
    height: 32px;
    border: 1px solid $white;
    background: transparent;
    color: $white;
    margin-right: 8px;
    font-weight: $weight-bold;
    font-size: $size-6;
    padding: 0;
    flex-shrink: 0;
  }

  .caption {
    font-size: $size-7;
  }

  .item {
    align-items: center;

    &:not(.is-flex) {
      // display: inline-block;
      // text-align: center;

      .tag {
        margin-right: 0;
        margin-bottom: 8px;
      }
    }
  }

  // sizes

  &.is-small {
    .tag {
      width: 24px;
      height: 24px;
      margin-right: 12px;
      // border-color: transparent;
    }

    .caption {
      font-size: $size-6;
    }
  }

  &.is-large {
    .tag {
      width: 48px;
      height: 48px;
      margin-right: 16px;
      font-size: $size-5;
    }
  }
}
</style>
