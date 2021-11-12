<template>
  <div>
    <h1 class="title is-1">Cont nou</h1>
    <br />

    <template v-if="$route.query.confirmation == null">
      <div class="form">
        <ValidationObserver v-slot="{ passes }" tag="form" @submit.prevent>
          <VField label="Nume și prenume" rules="required">
            <b-input v-model="name" />
          </VField>

          <VField label="E-mail" rules="required">
            <b-input v-model="email" />
          </VField>

          <VField label="Parola" rules="required" name="password">
            <b-input v-model="password" type="password" />
          </VField>

          <VField label="Repetă parola" rules="required|confirmed:password">
            <b-input v-model="re_password" type="password" />
          </VField>

          <b-button
            native-type="submit"
            class="button-submit is-primary"
            @click="passes(submit)"
          >
            Trimite
          </b-button>
        </ValidationObserver>
      </div>
    </template>

    <div v-else>
      <div class="subtitle">
        Veți primi un e-mail care conține un link de activare al contului.<br />

        Dacă nu primiți mesajul în 10 minute, verificați în Spam sau trimiteți
        din nou folosind butonul de mai jos.
      </div>
      <br />
      <br />

      <b-button class="is-primary" @click="resend">
        Trimite din nou link de activare
      </b-button>
    </div>
  </div>
</template>

<script>
import UserService from '@/services/user'
import { ToastService } from '@/services/buefy'

export default {
  name: 'AccountRegister',
  data() {
    return {
      name: '',
      email: '',
      password: '',
      re_password: '',
    }
  },
  methods: {
    submit() {
      this.$store
        .dispatch('registerUser', {
          name: this.name,
          email: this.email,
          password: this.password,
          re_password: this.re_password,
        })
        .then(() => {
          // console.log(response)
          this.$router.push({ query: { confirmation: this.email } })
        })
    },
    resend() {
      UserService.resend(this.$route.query.confirmation).then(() => {
        ToastService.open('Mesajul de confirmare a fost trimis din nou!')
      })
    },
  },
}
</script>
