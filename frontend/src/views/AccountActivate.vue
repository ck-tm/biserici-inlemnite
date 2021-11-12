<template>
  <div>
    <h1 class="title is-1">Activare cont</h1>
    <br />

    <div class="subtitle" v-if="status != null">
      <template v-if="status"> Contul a fost activat cu succes. </template>
      <template v-else>
        A apărut o problemă la activarea contului. Vă rugăm să încercați din nou
        sau să contactați administratorul.
      </template>
    </div>
  </div>
</template>

<script>
import UserService from '@/services/user'

export default {
  name: 'AccountActivate',
  data() {
    return {
      status: null,
    }
  },
  mounted() {
    UserService.activate(this.$route.params.uid, this.$route.params.token)
      .then(() => {
        this.status = true
      })
      .catch(() => {
        this.status = false
      })
  },
  methods: {},
}
</script>
