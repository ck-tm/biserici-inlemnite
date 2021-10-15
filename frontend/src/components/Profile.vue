<template>
  <div id="profile" v-if="profileShort">
    <b-button
      icon-left="close"
      type="is-black"
      class="close"
      @click="close"
    />

    <pre>{{ profileShort }}</pre>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'Profile',
  props: { active: Boolean },
  data() {
    return {}
  },
  computed: {
    ...mapGetters(['profileShort']),
  },
  mounted() {},
  methods: {
    close() {
      this.$store.commit('setProfileId', null)
    }
  },
}
</script>

<style lang="scss" scoped>
#profile {
  position: relative;
  width: 500px;
  // right: 100%;

  &.is-active {
  }

  /deep/.close {
  }
}
</style>
