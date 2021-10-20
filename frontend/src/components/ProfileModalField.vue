<template>
  <div class="profile-field columns">
    <div class="column is-3">
      <label class="label is-marginless">{{ label }}</label>
    </div>
    <div class="column">
      <template v-if="fields.length">
        <div
          v-for="field in fields"
          :key="'tab_subsection_field_' + field.key"
          class="subsection"
        >
          <label class="label is-small" v-text="field.label" />
          <div class="content has-text-weight-bold" v-html="field.value" />
          <pre
            class="has-background-primary has-text-black"
            v-if="field.elements.length"
            >{{ field.elements }}</pre
          >
        </div>
      </template>

      <template v-else>
        <div class="content" v-html="fields.value" />
        <pre
          class="has-background-primary has-text-black"
          v-if="fields.elements.length"
          >{{ fields.elements }}</pre
        >
      </template>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ProfileModalField',
  components: {},
  props: { label: String, fields: [Object, Array] },
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
.profile-field {
  padding: 0.75rem 30px;

  &:not(:last-child) {
    border-bottom: 1px solid #1f1f1f;
  }

  /deep/.content {
    color: #f6f6f6;

    p:not(:last-child) {
      margin-bottom: 8px;
    }

    p {
      font-size: $size-6;
      font-weight: normal;
    }
  }

  .subsection:not(:last-child) {
    margin-bottom: 1rem;
  }

  .label {
    color: #b8b8b8;
    margin-bottom: 4px;

    &.is-marginless {
      position: sticky;
      top: 0;
    }
  }

  pre {
    white-space: normal;
  }
}
</style>
