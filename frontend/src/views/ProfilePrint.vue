<template>
  <div class="" id="profileModal">
    <b-loading v-model="loading" />

    <div class="navbar">
      <div class="navbar-item">
        <img src="@/assets/logo_bis.png" />
        Biserici înlemnite
      </div>
    </div>

    <div class="profile-container" v-if="profile">
      <header>
        <div class="columns">
          <div class="column is-5">
            <div class="cod-monument" v-if="profile.cod">
              <div class="tag is-primary" v-text="'LMI'" />
              <div v-text="profile.cod" />
            </div>
            <h2 v-text="profile.title" />
          </div>
          <div class="column is-5">
            <div class="columns">
              <div class="column">
                <FilterDisplayItem
                  v-if="profile.conservare"
                  :value="profile.conservare"
                  index="conservare"
                  size="is-large"
                />
              </div>
              <div class="column">
                <FilterDisplayItem
                  v-if="profile.valoare"
                  :value="profile.valoare"
                  index="valoare"
                  size="is-large"
                />
              </div>
              <div class="column">
                <FilterDisplayItem
                  v-if="profile.prioritizare"
                  :value="profile.prioritizare"
                  index="prioritizare"
                  size="is-large"
                />
              </div>
            </div>
          </div>
        </div>
      </header>

      <div v-for="(tab, index) in profile.tabs" :key="'profile-tab-' + index">
        <template v-if="tab.type != 'embed'">
          <header class="has-text-centered">
            <h4>{{ tab.title }}</h4>
          </header>
          <ProfileModalTab v-bind="{ tab, print: true }" />
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'

import ProfileModalTab from '@/components/ProfileModalTab'
import FilterDisplayItem from '@/components/FilterDisplayItem'
import ApiService from '@/services/api'

export default {
  name: 'ProfileModal',
  components: { FilterDisplayItem, ProfileModalTab },
  props: {},
  data() {
    return {
      profile: null,
      tab: 0,
    }
  },
  computed: mapState(['loading']),
  mounted() {
    this.getProfile()
  },
  methods: {
    getProfile() {
      this.profile = null
      this.tab = 0
      this.$store.commit('setLoading', true)

      ApiService.get(`/map/${this.$route.params.id}/`).then((response) => {
        this.profile = response
        this.$store.commit('setLoading', false)

        // this.$nextTick(() => {
        //   window.print()
        // })
      })
    },
    close() {
      this.$router.push({
        name: 'Home',
        params: { id: this.$mq == 'mobile' ? null : this.$route.params.id },
      })
    },
  },
}
</script>

<style lang="scss" scoped>
#profileModal {
  .profile-container {
    flex: 1;
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
      flex: 1;

      @include desktop {
        overflow: hidden;
      }

      ul {
        padding-left: 32px;
        max-width: 100vw;

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
        background-color: #0f0f0f;
        padding: 0;
        overflow: visible;

        @include desktop {
          overflow: hidden;
        }

        .tab-item {
          overflow: visible;

          @include desktop {
            overflow: hidden;
            height: 100%;
          }
        }
      }
    }
  }
}
</style>
