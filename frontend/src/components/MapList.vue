<template>
  <div id="mapList">
    <h2>
      <b>{{ mapData.length }}</b>
      {{ mapData.length > 19 ? 'de' : '' }}
      {{ mapData.length > 1 ? 'biserici' : 'biserică' }}
    </h2>

    <b-table v-if="mapData" :data="mapData">
      <b-table-column
        custom-key="poza"
        v-slot="props"
        cell-class="has-text-weight-bold"
        sortable
      >
        <router-link :to="{ name: 'Home', params: { id: props.row.id } }">
          <div class="image">
            <img
              v-if="props.row.poze.length"
              class="row-thumb"
              :src="props.row.poze[0].poza.url"
              :alt="props.row.poze[0].poza.alt"
            />
          </div>
        </router-link>
      </b-table-column>

      <b-table-column
        field="title"
        label="Denumire"
        v-slot="props"
        cell-class="has-text-weight-bold"
        sortable
      >
        <router-link :to="{ name: 'Home', params: { id: props.row.id } }">
          {{ props.row.title }}
        </router-link>
      </b-table-column>

      <b-table-column
        field="judet"
        label="Localizare"
        v-slot="props"
        cell-class="is-size-6"
        sortable
      >
        <span v-if="props.row.judet">
          {{ filterValue('judet', props.row.judet) }},
        </span>
        <span v-if="props.row.localitate">
          {{ filterValue('localitate', props.row.localitate) }},
        </span>
        <span v-if="props.row.adresa">
          {{ props.row.adresa }}
        </span>
      </b-table-column>

      <b-table-column
        field="datare_prin_interval_timp"
        label="Datare"
        v-slot="props"
        cell-class="is-size-6"
        sortable
      >
        {{ props.row.datare_prin_interval_timp }}
      </b-table-column>

      <b-table-column
        field="conservare"
        label="Stare conservare"
        v-slot="props"
        width="160"
        sortable
      >
        <FilterDisplayItem
          v-if="props.row.conservare"
          index="conservare"
          :value="props.row.conservare"
          :hasLabel="false"
        />
      </b-table-column>

      <b-table-column
        field="valoare"
        label="Valoare patrimoniu"
        v-slot="props"
        sortable
      >
        <FilterDisplayItem
          v-if="props.row.valoare"
          index="valoare"
          :value="props.row.valoare"
          :hasLabel="false"
        />
      </b-table-column>

      <b-table-column
        field="prioritizare"
        label="Prioritizare"
        v-slot="props"
        sortable
      >
        <FilterDisplayItem
          v-if="props.row.prioritizare"
          index="prioritizare"
          :value="props.row.prioritizare"
          :hasLabel="false"
          :has-caption="false"
        />
      </b-table-column>
    </b-table>
  </div>
</template>

<script>
import FilterDisplayItem from '@/components/FilterDisplayItem'
import { mapState, mapGetters } from 'vuex'

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
    ...mapGetters(['filterValue']),
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
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 36;
  overflow: auto;
  padding: 24px;

  h2 {
    margin-bottom: 24px;
  }

  /deep/.table {
    th {
      font-size: $size-6;
      font-weight: normal;
      padding: 1rem 0.5rem;

      .th-wrap {
        // justify-content: center;
      }
    }

    td {
      vertical-align: middle;
      padding: 0.25rem 0.5rem;

      a {
        color: $white;

        &:hover {
          text-decoration: underline;
        }
      }

      .image {
        background-color: $grey-darker;
        width: 56px;
        height: 56px;
        margin-left: -0.5rem;
        overflow: hidden;

        img {
          object-fit: cover;
        }
      }
    }
  }
}
</style>
