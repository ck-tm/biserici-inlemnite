<template>
  <div>
    <h1>Intră în cont</h1>

    <div class="content">
      <br />
      <p>
        Utilizatorii înregistrați au acces la toate datele colectate în cadrul
        proiectului Biserici Înlemnite.
      </p>

      <p>
        Nu ai cont?
        <router-link to="/cont/inregistrare">Crează cont nou</router-link>
      </p>
    </div>

    <div class="form">
      <ValidationObserver v-slot="{ passes }" tag="form" @submit.prevent>
        <VField label="E-mail" rules="required">
          <b-input v-model="username" />
        </VField>

        <VField label="Parola" rules="required">
          <b-input v-model="password" type="password" />
        </VField>

        <div class="field">
          <b-button
            native-type="submit"
            class="button-submit is-primary"
            @click="passes(submit)"
          >
            Intră în cont
          </b-button>
        </div>
      </ValidationObserver>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AccountLogin',
  data() {
    return {
      username: '',
      password: '',
    }
  },
  methods: {
    submit() {
      this.$store.dispatch('login', {
        username: this.username,
        password: this.password,
      })
    },
  },
}
</script>
