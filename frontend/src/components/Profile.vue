<template>
  <div id="profile">
    <pre>{{ profile }}</pre>
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Profile',
  props: {
    profile: Object,
  },
  data() {
    return {}
  },
  computed: {
    ...mapState(['filters', 'grid']),
  },
  mounted() {},
  methods: {},
}
</script>

<style lang="scss" scoped>
#profile {
  right: 100%;

  &.is-active {
  }
}
</style>
