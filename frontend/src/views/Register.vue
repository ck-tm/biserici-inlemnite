<template>
  <div class="container container-page">
    <div class="content">
      <h3>
        <span v-if="!$route.params.success" v-text="$t('menu.register')" />
        <span v-else v-text="$t('register.thanks')" />
      </h3>
    </div>
    <br />

    <template v-if="!$route.params.success">
      <ValidationObserver ref="observer" slim>
        <div class="form">
          <section>
            <div class="title">
              <span class="tag">1</span>
              <span v-text="$t('register.1.title')" />
            </div>

            <VField grouped group-multiline>
              <b-radio-button
                v-for="(icon, key) in EntityIcons"
                :key="key"
                v-model="model.account_type"
                :native-value="key"
                type="is-white"
              >
                <b-icon class="is-size-4" :icon="icon" />
                <span v-text="$t(`entities.${key}`)" />
              </b-radio-button>
            </VField>

            <br />
            <br />
            <div class="columns is-multiline">
              <div class="column is-12">
                <VField>
                  <b-input
                    v-model="model.name"
                    :placeholder="$t('register.1.name')"
                  />
                </VField>
              </div>
              <div class="column is-6">
                <VField rules="required|email">
                  <b-input
                    v-model="model.email"
                    :placeholder="$t('register.1.email')"
                  />
                </VField>
              </div>
              <div class="column is-6">
                <VField rules="required">
                  <b-input
                    v-model="model.phone"
                    :placeholder="$t('register.1.phone')"
                  />
                </VField>
              </div>
            </div>
          </section>

          <section>
            <div class="title">
              <span class="tag">2</span>
              <span v-text="$t('register.2.title')" />
            </div>

            <VField grouped group-multiline v-if="domains">
              <b-checkbox-button
                v-for="domain of domains"
                :key="domain.id"
                :native-value="domain.id"
                v-model="model.profile_domains"
                :class="{
                  'is-selected': findId(domain.id),
                }"
                :style="{
                  ...(findId(domain.id) && {
                    background: domain.color,
                  }),
                }"
                :disabled="
                  model.profile_domains.length > 2 && !findId(domain.id)
                "
              >
                {{ domain.name }}
              </b-checkbox-button>
            </VField>

            <b-loading v-model="loading.domains" :is-full-page="false" />
          </section>

          <section>
            <div class="title">
              <div class="tag">3</div>
              <span v-text="$t('register.3.title')" />
            </div>

            <div class="columns">
              <div class="column is-6">
                <VField rules="">
                  <b-input
                    v-model="model.link"
                    placeholder="http://www.example.ro"
                  />
                </VField>
              </div>
            </div>
          </section>

          <section>
            <div class="title">
              <div class="tag">4</div>
              <span v-text="$t('register.4.title')" />
            </div>

            <div class="columns">
              <div class="column is-9">
                <VField rules="min:30|required">
                  <b-input
                    rows="6"
                    type="textarea"
                    :placeholder="$t('register.4.placeholder')"
                    v-model="model.bio"
                  />
                </VField>
              </div>
            </div>
          </section>
        </div>

        <div class="columns is-centered">
          <div class="column is-4">
            <br />
            <br />
            <b-button
              type="is-white is-fullwidth has-text-weight-medium"
              :loading="loading.submit"
              @click="checkForm"
            >
              {{ $t('register.submit') }}
            </b-button>
          </div>
        </div>
      </ValidationObserver>
    </template>

    <div class="columns" v-else>
      <div class="column">
        <div class="notification is-dark">
          {{ $t('register.moderation') }}
        </div>

        <br />
        <div class="column is-4 is-offset-4">
          <router-link
            :to="{ name: 'Home' }"
            class="button is-white has-text-weight-medium is-fullwidth"
          >
            <span v-text="$t('register.browse')" />
            <b-icon icon="arrow-forward" />
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ApiService from '@/services/api'
import { ValidationObserver } from 'vee-validate'
import { EntityIcons } from '@/services/utils'
import VField from '@/components/VField'

export default {
  name: 'Register',
  components: { VField, ValidationObserver },
  data() {
    return {
      EntityIcons,
      domains: null,
      loading: {
        domains: false,
        submit: false,
      },
      model: {
        account_type: null,
        name: null,
        email: null,
        phone: null,
        profile_domains: [],
        link: null,
        bio: null,
      },
    }
  },
  mounted() {
    this.loading.domains = true

    ApiService.get('/domains-name/').then((response) => {
      this.domains = response
      this.loading.domains = false
    })
  },
  methods: {
    findId(id) {
      return this.model.profile_domains.indexOf(id) != -1
    },
    checkForm() {
      const $form = this.$refs.observer

      $form.validate().then((success) => {
        if (!success) {
          setTimeout(() => {
            const errors = Object.entries($form.errors)
              .map(([key, value]) => ({ key, value }))
              .filter((error) => error['value'].length)

            this.$scrollTo($form.refs[errors[0]['key']].$el, { offset: -200 })
          }, 100)
        } else this.submit()
      })
    },
    submit() {
      this.loading.submit = true

      ApiService.post('/register/', this.model)
        .then(() => {
          this.loading.submit = false
          this.$router.push({ params: { success: 'success' } })
        })
        .catch((error) => {
          console.log(error.response)
          this.loading.submit = false
        })
    },
  },
}
</script>
