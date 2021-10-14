<template>
  <div id="map">
    <l-map
      v-if="bounds"
      v-bind="{ options, bounds }"
      :max-zoom="10"
      :min-zoom="7"
      @update:center="centerUpdate"
      @update:zoom="zoomUpdate"
    >
      <l-tile-layer :url="url" :attribution="attribution" />

      <template v-for="marker in mapData">
        <l-marker
          v-if="marker.latitudine && marker.longitudine"
          :key="'marker-' + marker.id"
          :lat-lng="getLatLng([marker.latitudine, marker.longitudine])"
        />
      </template>
    </l-map>
  </div>
</template>

<script>
import { latLngBounds, latLng } from 'leaflet'
import { LMap, LTileLayer, LMarker } from 'vue2-leaflet'
import { mapState } from 'vuex'

export default {
  name: 'Map',
  components: { LMap, LTileLayer, LMarker },
  data() {
    return {
      // url: 'https://tiles.stadiamaps.com/tiles/osm_bright/{z}/{x}/{y}{r}.png',
      // attribution:
      //   '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
      url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',

      options: {
        zoomSnap: 0.5,
      },
    }
  },
  computed: {
    ...mapState(['mapData']),
    bounds() {
      if (this.mapData) {
        const bounds = new latLngBounds(
          this.mapData
            .map((e) => [e.latitudine, e.longitudine])
            .filter((e) => e[0] != null && e[1] != null)
        )
        return bounds.pad(0.25)
      }

      return null
    },
  },
  mounted() {},
  methods: {
    getLatLng(latlng) {
      return new latLng(latlng)
    },
    zoomUpdate(zoom) {
      this.currentZoom = zoom
    },
    centerUpdate(center) {
      this.currentCenter = center
    },
  },
}
</script>

<style lang="scss" scoped></style>
