<template>
  <div id="filters-advanced" class="container-sidebar">
    <label class="label is-small has-text-grey-light">Filtrare avansată</label>

    <b-tabs
      v-model="active.tab"
      animation="slide-prev slide-next"
      animateInitially
      vertical
    >
      <b-button
        icon-left="close"
        type="is-black"
        class="close"
        @click="toggleTab"
        v-if="active.tab"
      />

      <b-tab-item key="tab-null" :visible="false"></b-tab-item>

      <b-tab-item
        v-for="section in filters"
        :key="'tab-' + section.key"
        class="is-full-height"
      >
        <template #header>
          <p>
            <span v-text="section.title" />
            <span class="tag is-black" v-if="filterModel[section.key]">
              ({{ counters[section.key] }})
            </span>
          </p>
          <b-icon icon="arrow-forward" />
        </template>

        <template #default>
          <div class="container-scroll">
            <h1 v-text="section.title" />

            <FiltersAdvancedSection
              v-model="filterModel[section.key]"
              :filters="section"
              @input="update(section.key)"
            />
          </div>
        </template>
      </b-tab-item>

      <div class="results" v-if="resultCount != null || loading">
        <b-button
          type="is-primary"
          class="has-text-weight-bold"
          :loading="loading"
          @click="applyFilters"
        >
          Vezi {{ resultCount }}
          {{ resultCount > 1 ? 'rezultate' : 'rezultat' }}
        </b-button>
      </div>
      <div class="results" v-else-if="resultCount == 0">
        <div class="is-inline-flex">Nu există niciun rezultat</div>
      </div>
    </b-tabs>

    <div class="filter-actions" v-if="filterTotalCount">
      <div class="results">
        <b>{{ filterTotalCount }}</b>
        {{ filterTotalCount > 1 ? 'filtre active' : 'filtru activ' }}
      </div>

      <b-button
        type="is-black"
        icon-left="trash"
        expanded
        @click="clearFilters"
      >
        Șterge filtrele
      </b-button>
    </div>
  </div>
</template>

<script>
import FiltersAdvancedSection from '@/components/FiltersAdvancedSection'
import ApiService from '@/services/api'
import { mapState } from 'vuex'

export default {
  name: 'FiltersAdvanced',
  components: { FiltersAdvancedSection },
  props: {
    filters: Array,
  },
  data() {
    return {
      active: { tab: 0 },
      filterModel: {},
      resultCount: null,
      counters: {},
      loading: false,
    }
  },
  computed: {
    ...mapState({ filterBasic: (state) => state.filterData.basic }),
    filterTotalCount() {
      return Object.keys(this.counters).reduce(
        (sum, e) => sum + this.counters[e],
        0
      )
    },
  },
  mounted() {},
  methods: {
    toggleTab() {
      if (this.active.tab) this.active.tab = 0
    },
    clearFilters() {
      this.filterModel = {}
      this.counters = {}
      this.resultCount = null

      this.applyFilters()
    },
    update(key) {
      // remove empty keys / create non-existent
      if (key) {
        if (!Object.keys(this.filterModel[key]).length) {
          this.$delete(this.filterModel, key)
          this.$delete(this.counters, key)
        } else
          this.$set(
            this.counters,
            key,
            Object.keys(this.filterModel[key]).length
          )
      }

      this.loading = true

      ApiService.post('/filters/preview/', {
        advanced: this.filterModel,
        basic: this.filterBasic,
      }).then((response) => {
        this.resultCount = response.count
        this.loading = false
      })
    },
    applyFilters() {
      this.$store.commit('setFiltersAdvanced', this.filterModel)
      this.active.tab = 0

      this.$emit('update')
    },
  },
}
</script>

<style lang="scss" scoped>
#filters-advanced {
  position: relative;
  padding-top: 160px;

  .label {
    padding-left: 32px;
  }

  .filter-actions {
    position: absolute;
    bottom: 0;
    width: 100%;
    padding: 24px 32px;
    background: $black;

    .results {
      background: $white;
      color: $black;
      border-radius: $radius-large;
      padding: 9px 0 7px 0;
      text-align: center;
      font-size: $size-6;
    }

    .button {
      font-size: $size-7;

      .icon {
        font-size: $size-4;
      }
    }
  }

  /deep/.b-tabs {
    overflow: visible;

    nav,
    ul {
      width: 100%;
    }

    &.is-vertical > .tabs {
      flex: 1;

      ul li {
        white-space: normal;

        a {
          justify-content: space-between;
          text-align: left;
          padding-left: 32px;
        }

        &.is-active a {
          font-weight: 700;
          color: $white;
          border-color: $white;
        }
      }
    }

    .tab-content {
      background: $black;
      position: absolute;
      left: calc(100% + 1px);
      width: 528px;
      top: 0;
      border-right: 1px solid $grey;
      padding: 0;
      z-index: 39;
      overflow: hidden;

      .close {
        right: 19px;
        top: 4px;
        z-index: 2;
        font-size: 32px;
        border: 0;
        color: $grey-lighter;
      }

      .container-scroll {
        padding: 24px 24px 80px 24px;

        h1 {
          padding: 56px 34px 56px;
        }

        .label.is-sticky {
          background: $black;
          position: sticky;
          top: -24px;
          z-index: 1;
          padding-top: 16px;
          padding-left: 0;
          padding-bottom: 16px;
          border-bottom: 1px solid $grey;
          font-weight: 700;
          margin-bottom: 0;
          margin-top: 24px;
        }
      }

      .results {
        position: absolute;
        bottom: 0;
        padding: 16px 16px 16px 56px;
        background-color: $grey;
        width: 100%;
        z-index: 3;

        .button {
          width: 176px;
        }
      }

      .collapse {
        .collapse-trigger .button {
          justify-content: space-between;
          padding: 16px 6px 16px 32px;
          border-bottom: 1px solid $grey;
          min-height: 60px;
          height: auto;
          transition: border-color 0.2s;
          white-space: normal;
          text-align: left;
          border-radius: 0;
          position: sticky;

          .icon {
            font-size: 24px;
            transition: transform 0.15s;
          }

          &.is-active {
            .icon {
              transform: rotate(45deg);
            }
          }

          &.is-selected {
            font-weight: 700;
            border-bottom: 1px solid $grey-lighter;

            .icon {
              color: $primary;
            }
          }
        }

        .collapse-content {
          padding-left: 80px;

          .field {
            padding: 16px 0;

            &.has-addons {
              padding: 0;
              flex-direction: column;
            }
          }

          .checkbox {
            padding: 8px 0;
          }
        }
      }
    }
  }
}
</style>
