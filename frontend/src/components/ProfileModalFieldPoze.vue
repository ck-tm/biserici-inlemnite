<template>
  <div>
    <b-carousel :autoplay="false" :indicator-inside="false">
      <b-carousel-item
        v-for="(image, index) in field.value"
        :key="'carousel-poze' + index"
      >
        <div class="image">
          <img
            :src="'https://biserici-inlemnite.ro' + image.poza.url"
            :alt="image.poza.alt"
          />
        </div>
      </b-carousel-item>
    </b-carousel>
  </div>
</template>

<script>
export default {
  name: 'ProfileModalFieldPoze',
  components: {},
  props: { field: Object },
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
/deep/.carousel {
  .image {
    img {
      height: 90vh;
      width: auto;
      margin: 0 auto;
    }
  }
}
</style>
