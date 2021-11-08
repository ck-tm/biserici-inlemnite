<template>
  <div>
    <h1 class="title is-1">Forgot password?</h1>

    <template v-if="$route.query.confirmation == null">
      <div class="subtitle">
        Enter your email address to receive further instructions
      </div>

      <div class="form">
        <ValidationObserver v-slot="{ passes }" tag="form" @submit.prevent>
          <VField label="Email" rules="required|email">
            <b-input v-model="email" placeholder="e@mail.com" />
          </VField>

          <b-button
            native-type="submit"
            class="button-submit is-primary"
            @click="passes(submit)"
          >
            Send request
          </b-button>
        </ValidationObserver>
      </div>
    </template>

    <template v-else>
      <div class="subtitle">
        You will receive an e-mail containing a password reset link. If you
        can't find it, please check your spam folder.
      </div>
    </template>
  </div>
</template>

<script>
import UserService from '@/services/user'

export default {
  name: 'AccountForgotPass',
  data() {
    return {
      email: '',
    }
  },
  methods: {
    submit() {
      UserService.resetPassword(this.email).then(() => {
        this.$router.replace({ query: { confirmation: this.email } })
      })
    },
  },
}
</script>
