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
        <div class="column is-5">
          <h2 v-text="profile.title" />
        </div>
        <div class="column is-5">
          <div class="columns">
            <div class="column">
              <FilterDisplayItem
                :value="1 || profile.conservare"
                index="conservare"
                size="is-large"
              />
            </div>
            <div class="column">
              <FilterDisplayItem
                :value="'B' || profile.valoare"
                index="valoare"
                size="is-large"
              />
            </div>
            <div class="column">
              <FilterDisplayItem
                :value="1 || profile.prioritizare"
                index="prioritizare"
                size="is-large"
              />
            </div>
          </div>
        </div>
      </header>
    </div>

    <b-loading v-model="loading" />
  </div>
</template>

<script>
import FilterDisplayItem from '@/components/FilterDisplayItem'
import { mapState } from 'vuex'
import ApiService from '@/services/api'

export default {
  name: 'ProfileModal',
  components: { FilterDisplayItem },
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
    header {
      padding: 32px;
    }
  }
}
</style>
