<template>
  <div
    class="filter-item"
    :class="{ [`is-${index}`]: true }"
    v-if="activeOption"
  >
    <div
      class="label is-small"
      v-text="basicFilters[index].label"
      v-if="hasLabel"
    />

    <div class="item" :class="{ 'is-flex': !isMultiline }">
      <div
        class="tag bullet"
        :class="classTag"
        v-text="activeOption.id"
        :style="tagStyle"
      />

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
  },
  data() {
    return {
      basicFilters: BasicFilters,
    }
  },
  mounted() {},
  methods: {
    compFunc(e) {
      return e.interval
        ? this.value >= e.interval[0] && this.value <= e.interval[1]
        : this.value == e.id
    },
  },
  computed: {
    activeOption() {
      return this.basicFilters[this.index].options.find((e) => this.compFunc(e))
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

      if (i == null) {
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
            color: '#FFFFFF',
            'font-size': 0,
            width: this.activeOption.size + 'px',
            height: this.activeOption.size + 'px',
            'margin-left': (24 - this.activeOption.size) / 2 + 'px',
            'margin-right': 12 + (24 - this.activeOption.size) / 2 + 'px',
          }
        else return { 'background-color': '#FFFFFF', color: '#000000' }
      }

      return null
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
