<template>
  <div class="container-scroll">
    <template v-if="tab.type == 'sections'">
      <div
        class="columns"
        v-for="(section, index) in tab.sections"
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
              :print="print"
            />
          </template>

          <template v-else>
            <ProfileModalField
              v-for="field in section.fields"
              :key="'profile-section-field-' + field.key"
              :label="field.label"
              :fields="field"
              :print="print"
            />
          </template>
        </div>
      </div>
    </template>

    <template v-if="tab.type == 'embed'">
      <div class="container-iframe" v-html="tab.embed" />
    </template>
  </div>
</template>

<script>
import ProfileModalField from '@/components/ProfileModalField'
// import { mapState } from 'vuex'
// import ApiService from '@/services/api'

export default {
  name: 'ProfileModalTab',
  components: { ProfileModalField },
  props: { tab: Object, print: { type: Boolean, default: false } },
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

        @media print {
          padding: 0;
        }
      }
    }
  }
}

@media print {
  /deep/.profile-field {
    // break-inside: avoid-page;
  }
}

.container-iframe {
  height: 100%;
  width: 100%;

  /deep/.sketchfab-embed-wrapper {
    height: 100%;
    width: 100%;

    iframe {
      height: 100%;
      width: 100%;
    }
  }
}
</style>
