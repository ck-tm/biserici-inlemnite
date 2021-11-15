<template>
  <div>
    <b-input
      placeholder="Caută"
      icon="search"
      v-model="query"
      @input="search"
      :loading="searching"
      class="search-input"
      expanded
    />
  </div>
</template>

<script>
import ApiService from '@/services/api'

export default {
  name: 'NavSearch',
  data() {
    return {
      query: null,
      timeout: null,
      results: null,
      searching: false,
    }
  },
  methods: {
    search() {
      if (this.timeout) clearTimeout(this.timeout)
      this.timeout = setTimeout(() => {
        if (this.query.trim().length < 2) {
          this.results = null
          return
        }

        this.searching = true

        ApiService.get('/map?query=' + this.query.trim())
          .then((response) => {
            this.searching = false
            this.results = response
            // this.$store.commit('setFiltersBasic', null)
            // this.$store.commit('setFiltersAdvanced', null)
            this.$store.commit('setMapData', response)
          })
          .catch(() => {
            this.searching = false
          })
      }, 650)
    },
  },
  watch: {},
}
</script>

<style lang="scss" scoped>
/deep/.search-input {
  width: 248px;

  .input {
    border-radius: 0;
    border: 0;
    border-bottom: 1px solid transparent;
    background-color: transparent;

    &:hover,
    &:focus {
      // border-bottom: 1px solid $grey;
    }
  }

  .icon {
    color: $white;
    font-size: $size-3;
  }
}
</style>
