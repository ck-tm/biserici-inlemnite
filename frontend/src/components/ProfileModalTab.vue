<template>
  <div class="container-scroll">
    <div
      class="columns"
      v-for="(section, index) in sections"
      :key="'tab_section_' + index"
    >
      <div class="column is-3 has-label">
        <h4>{{ section.title }}</h4>
      </div>

      <div class="column is-9">
        <template v-if="section.subsections.length">
          <ProfileModalField
            v-for="(subsection, sIndex) in section.subsections"
            :key="'profile-section-field-' + sIndex"
            :label="subsection.title"
            :fields="subsection.fields"
          />
        </template>

        <template v-else>
          <ProfileModalField
            v-for="field in section.fields"
            :key="'profile-section-field-' + field.key"
            :label="field.label"
            :fields="field"
          />
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import ProfileModalField from '@/components/ProfileModalField'
// import { mapState } from 'vuex'
// import ApiService from '@/services/api'

export default {
  name: 'ProfileModalTab',
  components: { ProfileModalField },
  props: { sections: Array },
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
.container-scroll {
  padding: 0.75rem;
}

.columns {
  .column {
    border-bottom: 1px solid $grey;

    &.has-label {
      border-right: 1px solid $grey;

      h4 {
        padding: 10px 0 9px 32px;
        position: sticky;
        top: 0;
      }
    }
  }
}
</style>
