<template>
  <div>
    <nav class="navbar is-fixed-top">
      <div class="container is-fullhd">
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item">
            <img src="@/assets/logo_bis.png" />
            Biserici înlemnite
          </router-link>

          <a
            role="button"
            class="navbar-burger"
            @click="active.menu = !active.menu"
          >
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div class="navbar-menu" :class="{ 'is-active': active.menu }">
          <div class="navbar-start">
            <div class="navbar-item" v-if="this.$mq != 'mobile'">
              <NavSearch />
            </div>
          </div>
          <div class="navbar-end">
            <router-link to="/" class="navbar-item">Home</router-link>
            <router-link to="/about" class="navbar-item">
              Despre proiect
            </router-link>

            <a
              @click="logout"
              class="navbar-item has-text-primary"
              v-if="token != null"
            >
              Logout
            </a>

            <router-link
              to="/account/login"
              class="navbar-item has-text-primary"
              v-else
            >
              Intră în cont / Înregistrare
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
  data() {
    return {
      active: { menu: false },
    }
  },
  computed: mapState(['loading', 'token']),
  methods: {
    logout() {
      this.$store.dispatch('logout')
    },
  },
  afterRouteUpdate() {
    this.active.menu = false
  },
}
</script>
