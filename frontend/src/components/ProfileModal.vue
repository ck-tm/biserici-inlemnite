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
      <header>
        <div class="columns">
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
        </div>
      </header>

      <b-tabs v-model="tab" animation="slide-prev slide-next" animateInitially>
        <b-tab-item
          v-for="(tab, index) in profile.tabs"
          :key="'profile-tab-' + index"
        >
          <template #header>
            <b>{{ tab.title }}</b>
          </template>

          <template #default>
            <ProfileModalTab :sections="tab.sections" />
          </template>
        </b-tab-item>
      </b-tabs>
    </div>

    <b-loading v-model="loading" />
  </div>
</template>

<script>
import ProfileModalTab from '@/components/ProfileModalTab'
import FilterDisplayItem from '@/components/FilterDisplayItem'
import { mapState } from 'vuex'
import ApiService from '@/services/api'

export default {
  name: 'ProfileModal',
  components: { FilterDisplayItem, ProfileModalTab },
  props: { active: Boolean },
  data() {
    return {
      loading: false,
      profile: null,
      tab: 0,
    }
  },
  computed: {
    ...mapState({ profileId: (state) => state.profile.id }),
  },
  mounted() {},
  methods: {
    getProfile() {
      this.profile = null
      this.tab = 0
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
    height: 100%;
    display: flex;
    flex-direction: column;

    header {
      padding: 32px;
      border-bottom: 1px solid $border;
    }

    .container {
      display: flex;
      flex: 1;
    }

    /deep/.b-tabs {
      display: flex;
      flex-direction: column;
      overflow: hidden;
      flex: 1;

      ul {
        padding-left: 32px;

        li {
          font-size: $size-6;
          white-space: normal;

          &.is-active {
            a {
              color: $primary;
              border-bottom: 4px solid $primary;

              // background: $primary;
            }
          }

          a {
            padding: 24px 2px 20px;
            margin-right: 20px;
            border-bottom: 4px solid $black;
            margin-bottom: 0;
            line-height: $size-5;

            &:hover {
              border-bottom: 4px solid $primary;
            }
          }
        }
      }

      .tab-content {
        flex: 1;
        overflow: hidden;
        background-color: #0F0F0F;
        padding: 0;

        .tab-item {
          height: 100%;
          overflow: hidden;
        }
      }
    }
  }
}
</style>
