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
          <FilterDisplayItem
            v-if="basicFilters[index]"
            :index="index"
            :value="model && model.length ? model[0] : null"
            :has-label="false"
            :has-size-variation="true"
            :use-interval="false"
            size="is-small"
          />

          <span
            v-text="
              model && model.length
                ? options.find((e) => e.id == model[0]).value
                : 'Toate'
            "
            v-else
          />
        </b-button>
      </template>

      <b-dropdown-item :value="[]">
        <FilterDisplayItem
          v-if="basicFilters[index]"
          :index="index"
          :value="null"
          :has-label="false"
          size="is-small"
          :use-interval="false"
        />

        <span v-else>Toate</span>
      </b-dropdown-item>

      <b-dropdown-item
        v-for="item of options"
        :key="item.id"
        :value="[item.id]"
        aria-role="listitem"
      >
        <FilterDisplayItem
          v-if="basicFilters[index]"
          :index="index"
          :value="item.id"
          :has-label="false"
          :has-size-variation="true"
          :use-interval="false"
          size="is-small"
        />

        <span v-else>{{ item.value }}</span>
      </b-dropdown-item>
    </b-dropdown>
  </b-field>
</template>

<script>
import FilterDisplayItem from '@/components/FilterDisplayItem'

import { BasicFilters } from '@/services/utils'

export default {
  name: 'FiltersDropdown',
  components: { FilterDisplayItem },
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
