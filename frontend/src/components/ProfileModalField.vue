<template>
  <div class="profile-field columns">
    <div class="column is-3">
      <label class="label is-marginless">{{ label }}</label>
    </div>

    <div class="column">
      <div class="columns toggle-header" :class="{ 'is-gapless': print }">
        <div class="column">
          <ProfileModalFieldElement
            :label="fields.length > 1 ? fields[0].label : null"
            :value="fields.value || fields[0].value"
            :fieldElements="fields.length ? fields[0] : fields"
            :print="print"
          />
        </div>
        <div class="column is-narrow" v-if="fieldList.length && !print">
          <b-button
            type="is-black"
            size="is-small"
            icon-right="arrow-down"
            :class="{ 'is-active': active }"
            class="toggle-trigger"
            @click="active = !active"
          >
            Detalii
          </b-button>
        </div>
      </div>

      <div class="toggle-body" v-if="active || print">
        <ProfileModalFieldElement
          v-for="(field, index) in fieldList"
          :key="'profile-toggled-' + index"
          :label="field.label"
          :value="field.value"
          :print="print"
          :fieldElements="field"
          class="subsection"
        />
      </div>
    </div>
  </div>
</template>

<script>
import ProfileModalFieldElement from '@/components/ProfileModalFieldElement'

export default {
  name: 'ProfileModalField',
  components: { ProfileModalFieldElement },
  props: {
    label: String,
    fields: [Object, Array],
    print: { type: Boolean, default: false },
  },
  data() {
    return {
      active: false,
      fieldList: [],
    }
  },
  computed: {},
  mounted() {
    // if (!this.fields.length) console.log(this.fields)

    this.fieldList =
      this.fields.length > 1
        ? this.fields.slice(1)
        : this.fields.elements || this.fields[0].elements
  },
  methods: {},
  watch: {},
}
</script>

<style lang="scss" scoped>
.profile-field {
  &:not(:last-child) {
    border-bottom: 1px solid #1f1f1f;
    // border-bottom: 1px solid #FFF;
  }

  /deep/.label {
    color: #b8b8b8;

    &.is-marginless {
      padding: 12px 0 12px 30px;
      position: sticky;
      top: 0;

      @media print {
        padding: 0;
      }
    }
  }

  .toggle-header {
    padding: 0 0 0 30px;

    @media print {
      padding: 0;
      margin-bottom: 0 !important;
    }

    @include desktop {
      padding: 12px 0;
    }

    /deep/.toggle-trigger {
      padding: 0;
      height: auto;
      color: $primary;
      background: transparent;

      @include desktop {
        padding: 0 12px;
      }

      &.is-active {
        .icon {
          transform: rotate(180deg);
        }
      }
    }
  }

  .toggle-body {
    margin-bottom: 12px;
    margin-top: -12px;
    padding: 0 0 0 32px;

    @include desktop {
      padding: 0;
    }

    @media print {
      margin-top: 0;
      margin-bottom: 0;
      padding: 0;
    }
  }

  .subsection:not(:last-child) {
    margin-bottom: 1rem;
  }
}
</style>
