<template>
  <div>
    <div
      v-if="fieldElements.length > 1"
      :class="{ 'has-elements': fieldElements.length > 1 }"
    >
      <ProfileModalFieldComponent
        v-for="(element, index) in fieldElements"
        :key="'profile-section-element-field' + index"
        :field="element"
        :print="print"
        class="field-element"
      />
    </div>

    <template v-else>
      <ProfileModalFieldComponent :field="{ ...fieldElements, label, value }" :print="print" />
    </template>
  </div>
</template>

<script>
import ProfileModalFieldComponent from '@/components/ProfileModalFieldComponent'
export default {
  name: 'ProfileModalFieldElement',
  components: { ProfileModalFieldComponent },
  props: {
    label: String,
    fieldElements: [Object, Array],
    value: null,
    print: { type: Boolean, default: false },
  },
  data() {
    return {}
  },
  computed: {},
  mounted() {},
  methods: {},
  watch: {},
}
</script>

<style lang="scss" scoped>
.has-elements {
  // border: 1px solid $border;
  border: 1px solid $border;
  border-radius: $radius;
  padding: 16px;
}

.field-element {
  &:not(:last-child) {
    margin-bottom: 16px;
    // border-bottom: 1px dashed $border;
  }
}
</style>
