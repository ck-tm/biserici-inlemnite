<template>
  <div class="container is-fullhd" v-if="about">
    <div class="container-sidebar is-hidden-touch">
      <p class="label">Proiect sub egida</p>

      <div class="image">
        <img src="@/assets/logo-asociatia-vernacular.png" />
      </div>

      <div class="image">
        <img src="@/assets/logo-afcn.png" />
      </div>
    </div>

    <div class="container-page">
      <div class="images">
        <img src="@/assets/about-img1.jpg" />
        <img src="@/assets/about-img2.jpg" />
        <img src="@/assets/about-img3.jpg" />
        <img src="@/assets/about-img4.jpg" />
        <img src="@/assets/about-img5.jpg" />
        <img src="@/assets/about-img6.jpg" />
        <img src="@/assets/about-img7.jpg" />
      </div>

      <h1 v-text="about.title" />

      <section v-for="(body, index) in about.body" :key="'about-body-' + index">
        <div v-html="body" class="content" />
      </section>

      <div class="section-partners" v-if="about.parteneri">
        <div class="content">
          <h2>Parteneri</h2>

          <div class="columns is-multiline is-gapless">
            <a
              v-for="(item, index) in about.parteneri"
              :key="'about-logos-' + index"
              :href="item.link"
              target="_blank"
              class="column is-3 image"
            >
              <img
                :src="'https://beta.biserici-inlemnite.ro' + item.logo.url"
                :alt="item.logo.alt"
              />
            </a>
          </div>
        </div>
      </div>
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
}

.container-sidebar {
  padding: 277px 48px 48px 48px;

  .label {
    font-size: 10px;
    text-transform: uppercase;
    font-weight: $weight-bold;
  }

  .image {
    margin-bottom: 40px;
  }
}

.images {
  display: flex;
  overflow: hidden;

  img {
    height: 256px;
    width: auto;
  }
}

.section-partners {
  background-color: #fff;
  color: $black;
  padding: 24px;

  @include desktop {
    padding: 80px 100px;
  }

  h2 {
    color: $black;
  }

  .image {
    border: 1px solid $white;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 120px;
    margin: 0 -1px -1px 0 !important;

    img {
      max-height: 95%;
      width: auto;
    }

    &:hover {
      opacity: 0.7;
    }
  }
}
</style>
