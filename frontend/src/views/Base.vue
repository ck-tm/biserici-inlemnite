<template>
  <div>
    <nav class="navbar is-fixed-top">
      <div class="container is-fullhd">
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item">
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
            <router-link to="/" class="navbar-item">Despre proiect</router-link>
          </div>
        </div>
      </div>
    </nav>

    <div class="container-fluid">
      <router-view />
    </div>
  </div>
</template>

<script>
import NavSearch from '../components/NavSearch'

export default {
  name: 'Base',
  components: {
    NavSearch,
  },
}
</script>
