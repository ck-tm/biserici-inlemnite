<template>
  <div>
    <label v-if="field.label" class="label" v-text="field.label" />

    <template v-if="getType == 'poze'">
      <b-button
        size="is-small"
        icon-left="images"
        class="button-link"
        @click="openModalPoze"
      >
        Vezi {{ field.value.length }}
        {{ field.value.length == 1 ? 'poză' : 'poze' }}
      </b-button>
    </template>

    <template v-else>
      <div
        class="content has-text-weight-bold"
        v-html="$options.filters.formatFieldValue(field.value)"
      />
    </template>
  </div>
</template>

<script>
import ProfileModalFieldPoze from '@/components/ProfileModalFieldPoze'
import { BooleanOptions } from '@/services/utils'

export default {
  name: 'ProfileModalFieldComponent',
  components: {},
  props: { field: Object },
  data() {
    return {
      getType: this.field.type || 'normal',
      booleanOptions: BooleanOptions,
    }
  },
  computed: {},
  mounted() {},
  methods: {
    openModalPoze() {
      this.$buefy.modal.open({
        parent: this,
        component: ProfileModalFieldPoze,
        customClass: 'modal-poze',
        trapFocus: true,
        // width: '40vw',
        props: {
          field: this.field,
        },
      })
    },
    // toggleGallery(value) {
    //   this.gallery = value

    //   if (value) {
    //     return document.documentElement.classList.add('is-clipped')
    //   } else {
    //     return document.documentElement.classList.remove('is-clipped')
    //   }
    // },
  },
  watch: {},
}
</script>

<style lang="scss" scoped>
.label {
  font-size: $size-7;

  &:not(:last-child) {
    margin-bottom: 4px;
  }
}

.content {
  color: #f6f6f6;

  /deep/p {
    font-size: $size-6;
    font-weight: normal;

    &:not(:last-child) {
      margin-bottom: 4px;
    }
  }
}

/deep/.button-link {
  font-weight: 700;
  color: $primary;
  background: $black;
  border: 0;
  padding: 0;
  height: auto;

  .icon.is-small {
    color: $white;
    font-size: $size-3;
    height: $size-6;
  }
}
</style>
