<template>
  <div id="profilePreview" v-if="profilePreview">
    <b-button
      icon-left="close"
      type="is-black"
      size="is-size-2"
      class="close"
      @click="close"
    />

    <div class="container-profile container-scroll">
      <div class="images columns is-variable is-2">
        <div
          class="column is-6"
          v-for="(image, index) in profilePreview.poze"
          :key="'images_' + index"
        >
          <div class="image is-square">
            <img :src="image.poza.url" :alt="image.poza.alt" />
          </div>
        </div>
      </div>

      <h3 v-text="profilePreview.title" />
      <p>
        <span
          v-if="profilePreview.adresa"
          v-text="profilePreview.adresa + ', '"
        />
        <span
          v-if="profilePreview.localitate"
          v-text="filterValue('localitate', profilePreview.localitate) + ', '"
        />
        <span
          v-if="profilePreview.judet"
          v-text="'jud. ' + filterValue('judet', profilePreview.judet)"
        />
      </p>

      <hr />

      <label class="label is-small" v-text="'Perioada'" />
      <p v-text="profilePreview.datare_prin_interval_timp" />

      <hr />

      <div class="columns">
        <div class="column">
          <FilterDisplayItem
            :value="profilePreview.conservare"
            index="conservare"
            size="is-large"
            is-multiline
          />
        </div>
        <div class="column">
          <FilterDisplayItem
            :value="profilePreview.valoare"
            index="valoare"
            size="is-large"
            is-multiline
          />
        </div>
        <div class="column">
          <FilterDisplayItem
            :value="profilePreview.prioritizare"
            index="prioritizare"
            size="is-large"
            is-multiline
          />
        </div>
      </div>
    </div>

    <div class="bottom">
      <b-button type="is-primary" @click="$emit('openProfileModal')">
        Află mai multe
      </b-button>
    </div>
  </div>
</template>

<script>
import FilterDisplayItem from '@/components/FilterDisplayItem'
import { mapGetters } from 'vuex'

export default {
  name: 'ProfilePreview',
  components: { FilterDisplayItem },
  props: { active: Boolean },
  data() {
    return {}
  },
  computed: {
    ...mapGetters(['profilePreview', 'filterValue']),
  },
  mounted() {},
  methods: {
    close() {
      this.$router.push({ name: 'Home', params: { id: null } })
    },
  },
}
</script>

<style lang="scss" scoped>
#profilePreview {
  position: relative;
  width: 500px;
  z-index: 37;
  background-color: $black;

  .close {
    top: 12px;
    right: 12px;
  }

  .images {
    display: flex;

    .image {
      img {
        background-color: $grey;
        object-fit: cover;
      }
    }
  }

  .container-profile {
    padding: 64px 24px 104px 24px;
  }

  .bottom {
    position: absolute;
    left: 0;
    bottom: 0;
    width: 100%;
    border-top: 1px solid $border;
    padding: 16px 24px;
    background-color: $black;
    z-index: 1;

    .button {
      font-weight: $weight-bold;
      width: 176px;
    }
  }
}
</style>
