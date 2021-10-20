<template>
  <div id="map">
    <l-map
      ref="map"
      v-if="bounds"
      v-bind="{ options, bounds, maxBounds: bounds }"
    >
      <l-tile-layer :url="url" :attribution="attribution" />
      <l-control-zoom position="bottomright" />

      <template v-for="marker in mapData">
        <l-marker
          v-if="marker.latitudine && marker.longitudine"
          :key="'marker-' + marker.id"
          :icon="getIcon(marker)"
          :lat-lng="getLatLng([marker.latitudine, marker.longitudine])"
          @click="openProfile(marker)"
        />
      </template>
    </l-map>
  </div>
</template>

<script>
import { icon, latLngBounds, latLng } from 'leaflet'
import { LMap, LTileLayer, LMarker, LControlZoom } from 'vue2-leaflet'
import { Colors } from '@/services/utils'
import { mapState } from 'vuex'

import 'leaflet/dist/leaflet.css'

export default {
  name: 'Map',
  components: { LMap, LTileLayer, LMarker, LControlZoom },
  data() {
    return {
      // url: 'https://tiles.stadiamaps.com/tiles/osm_bright/{z}/{x}/{y}{r}.png',
      // attribution:
      //   '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>, &copy; <a href="https://openmaptiles.org/">OpenMapTiles</a> &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors',
      // url: 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
      url: 'http://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png',
      attribution:
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',

      options: {
        zoomSnap: 0.5,
        zoomControl: false,
        minZoom: 7,
        maxZoom: 15,
      },
      icon: {
        size: [29, 37],
        anchor: [14, 37],
      },
    }
  },
  computed: {
    ...mapState({
      mapData: (state) => state.mapData,
      profileId: (state) => state.profile.id,
    }),
    bounds() {
      if (this.mapData && this.mapData.length) {
        const bounds = new latLngBounds(
          this.mapData
            .map((e) => [e.latitudine, e.longitudine])
            .filter((e) => e[0] && e[1])
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

    getMarkerIcon(color) {
      return (
        'data:image/svg+xml;base64,' +
        btoa(
          `<svg xmlns="http://www.w3.org/2000/svg"><mask id="a" fill="#fff"><path fill-rule="evenodd" clip-rule="evenodd" d="M18.44 28.87c.111-.291.353-.513.65-.611C24.848 26.339 29 20.904 29 14.5 29 6.492 22.508 0 14.5 0S0 6.492 0 14.5c0 6.404 4.152 11.838 9.91 13.759.297.098.538.32.65.612l3.005 7.917c.327.86 1.543.86 1.87 0l3.005-7.917z"/></mask><path fill-rule="evenodd" clip-rule="evenodd" d="M18.44 28.87c.111-.291.353-.513.65-.611C24.848 26.339 29 20.904 29 14.5 29 6.492 22.508 0 14.5 0S0 6.492 0 14.5c0 6.404 4.152 11.838 9.91 13.759.297.098.538.32.65.612l3.005 7.917c.327.86 1.543.86 1.87 0l3.005-7.917z" fill="${color}"/><path d="M13.565 36.788l1.87-.71-1.87.71zM10.56 28.87l1.87-.71-1.87.71zm7.882 0l-1.87-.71 1.87.71zM27 14.5c0 5.518-3.576 10.205-8.543 11.861l1.265 3.795C26.273 27.972 31 21.79 31 14.5h-4zM14.5 2C21.404 2 27 7.596 27 14.5h4C31 5.387 23.613-2 14.5-2v4zM2 14.5C2 7.596 7.596 2 14.5 2v-4C5.387-2-2 5.387-2 14.5h4zm8.543 11.861C5.576 24.705 2 20.018 2 14.5h-4c0 7.29 4.727 13.472 11.278 15.656l1.265-3.795zm4.892 9.717l-3.006-7.917-3.74 1.42 3.006 7.917 3.74-1.42zm1.136-7.917l-3.006 7.917 3.74 1.42 3.005-7.917-3.74-1.42zm-4.876 9.337c.98 2.58 4.63 2.58 5.61 0l-3.74-1.42c.327-.86 1.543-.86 1.87 0l-3.74 1.42zm-2.417-7.342a.96.96 0 01-.588-.575l3.74-1.42a3.041 3.041 0 00-1.887-1.8l-1.265 3.795zm9.18-3.795a3.04 3.04 0 00-1.887 1.8l3.74 1.42a.96.96 0 01-.589.575l-1.265-3.795z" fill="#fff" mask="url(#a)"/></svg>`
        )
      )
    },

    getIcon(marker) {
      return icon({
        iconUrl: this.getMarkerIcon(
          Colors.conservare[Math.round(marker.conservare)-1] || Colors.conservare[0]
        ),
        iconSize: this.icon.size,
        iconAnchor: this.icon.anchor,
      })
    },

    openProfile(marker) {
      this.$router
        .push({ name: 'Home', params: { id: marker.id } })
        .catch(() => {})
    },
  },
  watch: {
    profileId(vNew, vOld) {
      if (!vOld || !vNew)
        this.$nextTick(() => {
          if (!this.$refs.map) return

          this.$refs.map.mapObject.invalidateSize()

          if (vNew) {
            const marker = this.mapData.find((e) => e.id == vNew)

            this.$refs.map.mapObject.setView(
              this.getLatLng([marker.latitudine, marker.longitudine])
            )
          } else {
            this.$refs.map.mapObject.fitBounds(this.bounds)
          }
        })
    },
  },
}
</script>

<style lang="scss" scoped>
#map {
  flex: 1;

  /deep/.leaflet-container {
    .leaflet-pane {
      z-index: 36;
    }

    .leaflet-top,
    .leaflet-bottom {
      z-index: 37;
    }

    .leaflet-tile {
      filter: hue-rotate(30deg) saturate(2) brightness(0.85) !important;
    }

    .leaflet-control-zoom {
      a {
        background-color: $black;
        color: $white;
        width: 56px;
        height: 56px;
        line-height: 52px;
      }
    }
  }
}
</style>
