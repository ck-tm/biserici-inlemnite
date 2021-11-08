<template>
  <div class="container is-fullhd" v-if="about">
    <div class="container-sidebar"></div>

    <div class="container-page">
      <h1 v-text="about.title" />

      <section v-for="(body, index) in about.body" :key="'about-body-' + index">
        <div v-html="body.value" class="content" />
      </section>

      <section v-if="about.parteneri">
        <div class="content">
          <h2>Parteneri</h2>

          <div class="columns is-multiline is-variable is-3">
            <a
              v-for="(item, index) in about.parteneri"
              :key="'about-logos-' + index"
              :href="item.link"
              target="_blank"
              class="column is-narrow image"
            >
              <img
                :src="'https://biserici-inlemnite.ro' + item.logo.url"
                :alt="item.logo.alt"
              />
            </a>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'About',
  components: {},
  props: {},
  data() {
    return {}
  },
  computed: mapState(['about']),
  mounted() {
    if (!this.about) this.$store.dispatch('getData', 'about')
  },
  methods: {},
}
</script>

<style lang="scss" scoped>
section {
  &:not(:last-child) {
    border-bottom: 1px solid $grey;
  }

  .image {
    img {
      height: 80px;
      width: auto;
    }

    &:hover {
      opacity: 0.7;
    }
  }
}
</style>
