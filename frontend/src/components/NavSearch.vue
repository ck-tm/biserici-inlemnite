<template>
  <div>
    <b-dropdown>
      <template #trigger>
        <div class="field">
          <b-input
            placeholder="Caută"
            icon="search"
            v-model="query"
            @input="search"
            :loading="searching"
            expanded
          />
        </div>
      </template>

      <b-dropdown-item has-link aria-role="listitem" v-if="results">
        LINK ME UP, SCOTTY!
      </b-dropdown-item>

      <b-dropdown-item custom v-else>
        Introdu un termen pentru căutare
      </b-dropdown-item>
    </b-dropdown>
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

        ApiService.get('/search/?query=' + this.query.trim())
          .then((response) => {
            this.searching = false
            this.results = response
          })
          .catch(() => {
            this.searching = false
          })
      }, 300)
    },
  },
  watch: {},
}
</script>

<style lang="scss" scoped>
/deep/.dropdown {
  .control {
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
}
</style>
