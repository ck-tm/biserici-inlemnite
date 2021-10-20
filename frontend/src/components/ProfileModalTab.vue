<template>
  <div class="container-scroll">
    <div class="columns is-multiline">
      <template v-for="(section, index) in sections">
        <div class="column is-3 is-label" :key="'tab_section_' + index">
          <h4>{{ section.title }}</h4>
        </div>

        <div class="column is-9" :key="'tab_section_content_' + index">
          <template v-if="section.subsections.length">
            <ProfileModalField
              v-for="(subsection, sIndex) in section.subsections"
              :key="'profile_collapse_' + sIndex"
              :label="subsection.title"
              :fields="subsection.fields"
            />
          </template>

          <template v-else>
            <ProfileModalField
              v-for="field in section.fields"
              :key="'profile_collapse_' + field.key"
              :label="field.label"
              :fields="field"
            />
          </template>
        </div>
      </template>
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

    &.is-label {
      border-right: 1px solid $grey;
      padding: 0;

      h4 {
        padding-left: 32px;
        padding-top: 22px;
        padding-bottom: 22px;
        position: sticky;
        top: 0;
      }
    }
  }
}
</style>
