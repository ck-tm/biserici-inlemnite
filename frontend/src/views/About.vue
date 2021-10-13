<template>
  <div class="container container-page">
    <div class="content">
      <h3>The Resilience</h3>
      <br />
      <br />

      <div class="columns">
        <div class="column is-7">
          <div v-html="$t('about.text')" />
          <br />
          <i18n path="about.text_link" tag="p">
            <router-link :to="{ name: 'Register' }">
              {{ $t('menu.register') }}
            </router-link>
          </i18n>
        </div>
        <div class="column is-5">
          <p><b v-text="$t('about.team')" /></p>
          <p>
            Alexandra-Maria Rigler, Alex Iliescu, Andreea Iager-Tako, Andrei
            Drăcea, Bogdan Cotîrță, Costin Bleotu, Pepe Peralta Guerrero, Val
            Mureșan
          </p>
          <p><b v-text="$t('about.consultancy')" /></p>
          <p>
            Alexandru Ciobotă, Alexandru Lorinți, Ana Kun, Andreas Samuelsson,
            Atelier Bobar, Bianca Băilă, Cristian Boldișteanu, Diana Marincu,
            Dragoș Miștorică, Emilia Szuszmann, Gabriel Amza, Hotvath Octavian
            Nicolae, Levente Kozma, Lia Pfeiffer, Livia Coloji, Loredana Gaiță,
            Manu Anghelescu, Mihai Drăgan, Monica Diaconu, Ovidiu Hrin, Ovidiu
            Zimcea, Pusha Petrov, Roxana Puriș, Sasha Bodeanu, Seba Tătaru,
            Sorin Chiuzbaian, Zoltan Bereczi and many more.
          </p>
        </div>
      </div>

      <h3>Contact</h3>
      <br />
      <p>
        <a href="mailto:noi@resilience.community">noi@resilience.community</a>
        <br />
        <a href="tel:+40829281819">+40829281819</a>
      </p>
    </div>
  </div>
</template>
