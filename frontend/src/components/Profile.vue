<template>
  <div id="profile">
    <div class="box">
      <!-- <pre>{{ profile.connections }}</pre> -->

      <button
        class="delete"
        type="button"
        @click="$router.push({ params: { id: null } })"
      />

      <p class="icon-text is-size-3 has-text-weight-bold is-spaced">
        <b-icon :icon="getIcon()" />
        <span v-text="profile.name" />
      </p>

      <p class="links">
        <a target="_blank" :href="'//' + profile.link" v-text="profile.link" />
      </p>

      <p class="domains tags">
        <a
          v-for="domain in profile.domains"
          :key="domain.id"
          class="tag"
          :style="{ background: domain.color }"
          v-text="domain.name"
          @click.prevent="
            setFilter({ type: 'domains', id: domain.id, filterName: 'domain' })
          "
        />
      </p>

      <p class="bio">
        {{ profile.bio }}
      </p>

      <br /><br />
      <p class="head">Know-how</p>
      <p class="tags">
        <a
          v-for="skill in profile.skills"
          :key="skill.id"
          class="tag"
          v-text="skill.name"
          @click.prevent="
            setFilter({ type: 'skills', id: skill.id, filterName: 'skill' })
          "
        />
      </p>

      <p class="head">Connections</p>

      <div
        class="is-spaced"
        v-for="(list, type) in profile.connections"
        :key="type"
      >
        <b-dropdown :mobile-modal="false" :disabled="!list.length">
          <template #trigger>
            <button type="button" class="button is-light">
              <span
                class="has-text-weight-semibold is-extended"
                v-text="type[0].toUpperCase() + type.substring(1)"
              />
              <span v-text="list.length" />
              <b-icon icon="arrow-down"></b-icon>
            </button>
          </template>

          <b-dropdown-item
            v-for="profile in list"
            :key="profile.id"
            aria-role="listitem"
            @click="$router.push({ name: 'Home', params: { id: profile.id } })"
          >
            {{ profile.name }}
          </b-dropdown-item>
        </b-dropdown>
      </div>
    </div>
  </div>
</template>

<script>
import { EntityIcons } from '@/services/utils'
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
  metaInfo() {
    return {
      title: this.$t('meta_tags.profile_title', { name: this.profile.name }),
      meta: [
        {
          name: 'description',
          content: this.$t('meta_tags.profile_description', {
            name: this.profile.name,
          }),
        },
        {
          property: 'og:title',
          content: this.$t('meta_tags.profile_title', {
            name: this.profile.name,
          }),
        },
        {
          property: 'og:description',
          content: this.$t('meta_tags.profile_description', {
            name: this.profile.name,
          }),
        },
        { property: 'og:type', content: 'profile' },
        {
          property: 'og:url',
          content: 'https://theresilient.community/' + this.profile.id,
        },
        {
          property: 'og:image',
          content: '',
        },
      ],
    }
  },
  methods: {
    getIcon() {
      return EntityIcons[this.profile.account_type]
    },
    setFilter(filter) {
      const f = {
        types: [],
        domain: null,
        skill: null,
        ...this.filters,
      }

      f[filter.filterName] = this.grid[filter.type].find(
        (e) => e.id == filter.id
      )

      this.$router.push({ params: { id: null } }).then(() => {
        this.$store.commit('setFilters', f)
      })
    },
  },
  watch: {
    profile() {
      window.scrollTo(0, 0)
    },
  },
}
</script>

<style lang="scss" scoped>
#profile {
  position: fixed;
  z-index: 29;
  top: 70px;
  right: 0;
  left: 0;
  font-size: $size-6;
  pointer-events: none;

  .box {
    max-height: calc(100vh - 70px);
    overflow-y: auto;
    pointer-events: auto;
    position: relative;
    width: 100%;

    @include tablet {
      max-height: calc(100vh - 140px);
      // overflow-y: visible;
      width: 380px;
      margin: auto;
    }

    @include desktop {
      margin-top: 30px;
      margin-right: 20px;
    }

    /deep/ .dropdown-content {
      margin-bottom: 16px;
    }
  }

  .delete {
    position: absolute;
    right: 16px;
    top: 16px;
    background-color: $grey-light;
    transition: all 0.15s;
    height: 24px;
    max-height: 24px;
    width: 24px;
    max-width: 24px;

    &:hover {
      transform: scale(1.2) rotate(90deg);
      background-color: $grey;
    }
  }

  p.head {
    font-weight: 600;
    padding-bottom: 8px;
    border-bottom: 1px solid $grey;
    margin-bottom: 16px;
  }

  .links a {
    text-decoration: underline;
  }

  .tags {
    margin-top: 16px;
  }

  .is-spaced {
    margin-bottom: 6px;
  }
}
</style>
