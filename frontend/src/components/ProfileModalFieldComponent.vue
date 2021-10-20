<template>
  <div>
    <label v-if="field.label" class="label is-small" v-text="field.label" />

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
      <div class="content has-text-weight-bold" v-html="field.value" />
    </template>
  </div>
</template>

<script>
import ProfileModalFieldPoze from '@/components/ProfileModalFieldPoze'

export default {
  name: 'ProfileModalFieldComponent',
  components: {},
  props: { field: Object },
  data() {
    return { getType: this.field.type || 'normal', active: { gallery: false } }
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

  .icon {
    color: $white;
    font-size: $size-3;
  }
}
</style>
