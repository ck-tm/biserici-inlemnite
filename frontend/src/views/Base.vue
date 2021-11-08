<template>
  <div>
    <nav class="navbar is-fixed-top">
      <div class="container is-fullhd">
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item">
            <img src="@/assets/logo_bis.png" />
            Biserici înlemnite
          </router-link>
        </div>

        <div class="navbar-menu">
          <div class="navbar-start">
            <div class="navbar-item">
              <NavSearch />
            </div>
          </div>
          <div class="navbar-end">
            <router-link to="/" class="navbar-item">Home</router-link>
            <router-link to="/despre" class="navbar-item">
              Despre proiect
            </router-link>

            <router-link
              to="/cont/autentificare"
              class="navbar-item has-text-primary"
            >
              Intra in cont / Inregistrare
            </router-link>
          </div>
        </div>
      </div>
    </nav>

    <div id="main-interface" class="container-fluid">
      <router-view />
    </div>

    <b-loading v-model="loading" />
  </div>
</template>

<script>
import NavSearch from '@/components/NavSearch'
import { mapState } from 'vuex'

export default {
  name: 'Base',
  components: {
    NavSearch,
  },
  computed: mapState(['loading']),
}
</script>
