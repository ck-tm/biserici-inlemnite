<template>
  <div class="container container-page">
    <b-loading v-model="loading" />

    <div class="columns is-centered">
      <div class="column is-8">
        <div class="content">
          <h3 v-text="$t('menu.resources')" />
          <br />
          <p v-html="$t('resources')" />
        </div>
        <br />

        <div class="links">
          <a
            v-for="link in links"
            :key="link.id"
            :href="link.url"
            target="_blank"
            class="button is-dark is-fullwidth"
          >
            <span v-text="link.title" />
            <b-icon icon="arrow-forward" />
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ApiService from '@/services/api'

export default {
  name: 'Resources',
  data() {
    return {
      links: null,
      loading: true,
    }
  },
  mounted() {
    ApiService.get('/resources/')
      .then((response) => {
        this.links = response
        this.loading = false
      })
      .catch(() => {
        this.loading = false
      })
  },
}
</script>
