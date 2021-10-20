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
        <b-button icon-right="arrow-down" size="is-small" expanded>
          {{
            model && model.length
              ? (options || basicFilters[index].options).find(
                  (e) => e.id == model[0]
                ).value
              : basicFilters[index]
              ? basicFilters[index].default.value
              : 'Toate'
          }}
        </b-button>
      </template>

      <b-dropdown-item :value="[]">
        <template v-if="basicFilters[index]">
          <span
            class="icon-circle"
            v-bind="{ style: computeStyle() }"
            v-text="basicFilters[index].default.id"
          />
          <span v-text="basicFilters[index].default.value" />
        </template>

        <span v-else>Toate</span>
      </b-dropdown-item>

      <b-dropdown-item
        v-for="(item, i) of options || basicFilters[index].options"
        :key="item.id"
        :value="[item.id]"
        aria-role="listitem"
      >
        <template v-if="basicFilters[index]">
          <span
            class="icon-circle"
            v-bind="{ style: computeStyle(i) }"
            v-text="basicFilters[index].options[i].id"
          />
          <span v-text="basicFilters[index].options[i].value" />
        </template>

        <span v-else>{{ item.value }}</span>
      </b-dropdown-item>
    </b-dropdown>
  </b-field>
</template>

<script>
import { Colors, BasicFilters } from '@/services/utils'

export default {
  name: 'FiltersDropdown',
  props: {
    value: null,
    label: String,
    index: String,
    options: Array,
  },
  data() {
    return {
      model: this.value,
      basicFilters: BasicFilters,
      colors: Colors,
    }
  },
  mounted() {},
  methods: {
    computeStyle(i) {
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

      if (BasicFilters[this.index] && BasicFilters[this.index].options[i].size)
        return {
          'background-color': '#CCCCCC',
          'font-size': 0,
          width: BasicFilters[this.index].options[i].size + 'px',
          height: BasicFilters[this.index].options[i].size + 'px',
          'margin-left':
            (24 - BasicFilters[this.index].options[i].size) / 2 + 'px',
          'margin-right':
            12 + (24 - BasicFilters[this.index].options[i].size) / 2 + 'px',
        }

      return null
    },
  },
  watch: {
    value(val) {
      this.model = val
    },
  },
}
</script>

<style lang="scss" scoped>
.icon-circle {
}
</style>
