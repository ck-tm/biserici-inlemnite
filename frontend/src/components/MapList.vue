<template>
  <div id="mapList" v-if="mapData">
    <h2 v-if="mapData.length">
      <b>{{ mapData.length }}</b>
      {{ mapData.length > 19 ? 'de' : '' }}
      {{ mapData.length > 1 ? 'biserici' : 'biserică' }}
    </h2>

    <div v-else>Nu există biserici pentru această selecție.</div>

    <b-table
      v-if="mapData"
      :data="mapData"
      mobile-sort-placeholder="Sortează după"
    >
      <b-table-column
        custom-key="poza"
        v-slot="props"
        cell-class="has-text-weight-bold"
        :sortable="true"
      >
        <router-link
          :to="{ name: 'Profile', params: { id: props.row.id } }"
          class="image"
        >
          <img
            v-if="props.row.poze.length"
            class="row-thumb"
            :src="props.row.poze[0].poza.url"
            :alt="props.row.poze[0].poza.alt"
          />
        </router-link>
      </b-table-column>

      <b-table-column
        field="title"
        label="Denumire"
        v-slot="props"
        cell-class="has-text-weight-bold"
        :sortable="true"
      >
        <router-link
          :to="{ name: 'Profile', params: { id: props.row.id } }"
          class="underline-mobile"
        >
          {{ props.row.title }}
        </router-link>
      </b-table-column>

      <b-table-column
        field="judet"
        label="Localizare"
        v-slot="props"
        cell-class="is-size-6"
        :sortable="true"
      >
        <template v-if="props.row.judet"> {{ props.row.judet }}, </template>
        <template v-if="props.row.localitate">
          {{ props.row.localitate }},
        </template>
        <template v-if="props.row.adresa">
          {{ props.row.adresa }}
        </template>
      </b-table-column>

      <b-table-column
        field="datare"
        label="Datare"
        v-slot="props"
        cell-class="is-size-6"
        :sortable="true"
      >
        {{ props.row.datare }}
      </b-table-column>

      <b-table-column
        field="conservare"
        label="Stare conservare"
        v-slot="props"
        width="160"
        :sortable="true"
      >
        <FilterDisplayItem
          class="mobile-invert"
          v-if="props.row.conservare"
          index="conservare"
          :value="props.row.conservare"
          :has-label="false"
        />
      </b-table-column>

      <b-table-column
        field="valoare"
        label="Valoare patrimoniu"
        v-slot="props"
        :sortable="true"
      >
        <FilterDisplayItem
          class="mobile-invert"
          v-if="props.row.valoare"
          index="valoare"
          :value="props.row.valoare"
          :has-label="false"
        />
      </b-table-column>

      <b-table-column
        field="prioritizare"
        label="Prioritizare"
        v-slot="props"
        :sortable="true"
      >
        <FilterDisplayItem
          class="mobile-invert"
          v-if="props.row.prioritizare"
          index="prioritizare"
          :value="props.row.prioritizare"
          :has-label="false"
          :has-caption="false"
        />
      </b-table-column>
    </b-table>
  </div>
</template>

<script>
import FilterDisplayItem from '@/components/FilterDisplayItem'
import { mapState } from 'vuex'

export default {
  name: 'MapList',
  components: { FilterDisplayItem },
  data() {
    return {}
  },
  computed: {
    ...mapState({
      mapData: (state) => state.mapData,
      profileId: (state) => state.profile.id,
    }),
  },
  mounted() {},
  methods: {
    openProfile(marker) {
      this.$router
        .push({ name: 'Home', params: { id: marker.id } })
        .catch(() => {})
    },
  },
  watch: {},
}
</script>

<style lang="scss" scoped>
#mapList {
  background-color: $black;
  z-index: 36;
  overflow: auto;
  padding: 24px;

  @include desktop {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
  }

  h2 {
    margin-bottom: 24px;
  }

  /deep/.b-table {
    .table-mobile-sort {
      padding: 0 8px;

      .select {
        select {
          background-color: $grey-darker;
          border-color: $grey-light;
          padding-top: 0;
          padding-bottom: 0;
        }

        &:after {
          border-width: 2px;
        }
      }
    }

    th {
      font-size: $size-6;
      font-weight: normal;
      padding: 1rem 0.5rem;
    }

    td {
      vertical-align: middle;
      padding: 0.25rem 0.5rem;

      @include touch {
        font-size: $size-6;
        vertical-align: middle;

        &:last-child {
          padding-bottom: 16px;
          border-bottom: 1px solid $grey;
        }
      }

      a {
        color: $white;

        &:hover {
          text-decoration: underline;
        }
      }

      .image {
        background-color: $grey-darker;
        margin-left: -0.5rem;
        overflow: hidden;
        width: 100%;
        height: 180px;

        @include desktop {
          width: 56px;
          height: 56px;
        }

        img {
          object-fit: cover;
          height: 100%;
        }
      }
    }
  }
}
</style>
