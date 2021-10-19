<template>
  <div id="profileModal" v-if="active">
    <b-button
      icon-left="close"
      type="is-black"
      size="is-size-2"
      class="close"
      @click="close"
    />

    <div class="profile-container" v-if="profile">
      <header class="columns">
        <div class="column">
          <h2 v-text="profile.title" />
        </div>
        <div class="column"></div>
      </header>
    </div>

    <b-loading v-model="loading" />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import ApiService from '@/services/api'

export default {
  name: 'ProfileModal',
  components: {},
  props: { active: Boolean },
  data() {
    return {
      loading: false,
      profile: null,
    }
  },
  computed: {
    ...mapState({ profileId: (state) => state.profile.id }),
  },
  mounted() {},
  methods: {
    getProfile() {
      this.profile = null
      this.loading = true

      ApiService.get(`/map/${this.profileId}/`).then((response) => {
        this.profile = response
        this.loading = false
      })
    },
    close() {
      this.$emit('close')
      // this.$router.push({ name: 'Home', params: { id: null } })
    },
  },
  watch: {
    active(value) {
      if (value) this.getProfile()
    },
  },
}
</script>

<style lang="scss" scoped>
#profileModal {
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  z-index: 99;
  background-color: $black;

  .profile-container {
  }
}
</style>
