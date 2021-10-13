import Vue from 'vue'
import VueI18n from 'vue-i18n'

Vue.use(VueI18n)

const messages = {
  en: {
    home: {
      message:
        'The Resilience is an interactive tool, that aims to provide an image of the cultural and creative potential of Timisoara.',
      mobile_warning:
        'The mobile version is limited to a list view. Please use a desktop or tablet display for the full experience.',
      filters: 'Filters',
      showing_all: 'Showing all {total} results.',
      showing_of: 'Showing {filtered} of {total} results.',
      showing_none: 'No results. Please select a different filter.',
      showing: '{total} results',
    },
    meta_tags: {
      title: 'TheResilient community',
      // description: 'TheResilient community',
      profile_title: 'TheResilient profile of {name}',
      profile_description: 'Connect with {name} on TheResilient.community',
    },
    entities: {
      I: 'People',
      O: 'Organisations',
      P: 'Projects',
    },
    menu: {
      search: 'Search',
      language: 'Language',
      about: 'About',
      resources: 'Useful resources',
      register: 'Register',
    },
    register: {
      browse: 'Browse other profiles',
      thanks: 'Thank you for registering!',
      submit: 'Submit request',
      moderation: `Your profile will be reviewed by a moderator. You'll receive an e-mail as soon as we're done.`,
      1: {
        title: 'Which section better defines you?',
        name: 'Name',
        email: 'E-mail address',
        phone: 'Telephone',
      },
      2: {
        title: 'Select up to 3 categories which represent you',
      },
      3: {
        title: 'Link to one of your web profiles (optional)',
      },
      4: {
        title: 'A short description',
        placeholder: 'Write here...',
      },
    },
    resources: `
      TheResilient.Community is an exploratory project that aims to study
      the resilient manifestation of a vibrant local community like the one
      in Timișoara. A non-academic approach, the methodology focused on
      personal stories, specific expertise, this instrument being just one
      of many resources and know-how available on resilience that any active
      member of a community can activate at a personal, project or community
      level. <br /> The methodology and documents developed as a result of
      the project are available here.
    `,
    about: {
      team: 'Implementation team',
      consultancy: 'Consultancy',
      text: `
        <p>
          TheResilient.Community is a platform that collects and promotes local
          resilience manifestations, offering an explorative approach towards
          community behaviours that are at the base of adaptability, survival
          but also social innovation. <br/> This instrument doesn't aim to be a finite
          tool, but rather one that grows and changes organically depending on
          the communities' solutions, inspiring collaboration and sustainability
          when it comes to facing common challenges.
        </p>
        <p>
          Resilience has been for some time a buzz word since 2020 and a focus
          in a reality where development and growth is clearly not sustainable.
          Resilience is no longer just bouncing back from a bad situation, is
          also how you handle the situation while it develops, how you respond,
          plan and transform motivated to strive beyond it.
        </p>
        <p>
          With extensive on the ground community experience, bridging between
          very different communities, AMBASADA has teamed-up with Ashoka Romania
          to build together a new framework in which cities and areas can be
          solution seekers, change implementers and resilient masters in a
          future where external factors are less foreseable than ever before.
        </p>
      `,
      text_link: `
        If you wish to be part of the community or know someone who would
        benefit from being part of this community, please leave us your
        details by going to the {0} section.
        `,
    },
  },
  ro: {
    home: {
      message:
        'The Resilience este un instrument interactiv care dorește să reprezente o imagine a potențialului cultural și creativ al orașului Timișoara.',
      mobile_warning:
        'Versiunea de mobil este limitată la o listă. Folosește un dispozitiv cu ecran mai mare pentru experiența completă.',
      filters: 'Filtrare',
      showing_all: 'Vizualizezi {total} rezultate în total.',
      showing_of: 'Vizualizezi {filtered} din {total} rezultate în total.',
      showing_none: 'Nu există rezultate. Încearcă o altă filtrare.',
      showing: '{total} rezultate',
    },
    meta_tags: {
      title: 'TheResilient community',
      // description: 'The Resilience este un instrument interactiv care dorește să reprezente o imagine a potențialului cultural și creativ al orașului Timișoara.',
      profile_title: 'TheResilient profile of {name}',
      profile_description: 'Connect with {name} on TheResilient.community',
    },
    entities: {
      I: 'Oameni',
      O: 'Organizații',
      P: 'Proiecte',
    },
    menu: {
      search: 'Caută',
      language: 'Limba',
      about: 'Despre',
      resources: 'Resurse utile',
      register: 'Înscrie-te',
    },
    register: {
      browse: 'Vezi alte profile',
      thanks: 'Îți mulțumim pentru interes!',
      submit: 'Trimite cerere',
      moderation: `Profilul tău va fi revizuit de către un moderator. Vei primi un e-mail în curând.`,
      1: {
        title: 'Ce secțiune te definește mai bine?',
        name: 'Denumire',
        email: 'Adresa de e-mail',
        phone: 'Telefon',
      },
      2: {
        title: 'Alege până la 3 categorii reprezentative',
      },
      3: {
        title: 'Link către spațiul tău pe web (opțional)',
      },
      4: {
        title: 'O descriere scurtă',
        placeholder: 'Scrie aici...',
      },
    },
    resources: `
      TheResilient.Community este un proiect explorator care și-a propus să
      studieze manifestarea rezilienței la nivelul unei comunități
      virbrante, așa cum sunt ele găzduite de Timișoara. O abordare
      non-academică, ci concentrată pe povești personale și experiențe
      specifice, instrumentul acesta este doar una dintre multiplele resurse
      și informații legate de reziliență pe care le putem folosi ca și
      membri activi ai comunităților noastre. <br />
      Metodologia și materialele dezvoltate sunt disponibile aici.
    `,
    about: {
      team: 'Echipa de implementare',
      consultancy: 'Consultanță',
      text: `
        <p>
          TheResilient.Community este o platformă care colectează și promovează
          exemple de reziliență locală, oferind astfel un model explorator de
          studiu al comportamentelor comunitare ce asigură adaptabilitate,
          supraviețuire dar și inovare socială. <br/> Acest instrument nu își propune
          a fi exhaustiv, ci din contră, să crească și să se dezvolte organic,
          odată cu soluțiile găsite de comunitate, inspirând spre colaborare și
          sustenabilitate în fața provocărilor comune.
        </p>

        <p>
          Reziliența a devenit un cuvânt foarte des asociat cu pandemia începută
          în 2020, dar este un mușchi pe care orice comunitate trebuie să îl
          exerseze continuu, în diferite situații și contexte pentru a se
          asigura că este funcțională, incluzivă și se dezvoltă.
        </p>

        <p>
          Proiectul TheResilient.Community este inițiat de AMBASADA în
          colaborare cu Ashoka România și s-a concentrat pe mai multe etape de
          studiu: interviuri, focus groups concentrate, workshop-uri de validare
          și testare, precum și o evaluare de progres.
        </p>
      `,
      text_link: `
        Dacă doriți să intrați în comunitate sau să nominalizați pe cineva
        căruia această comunitate i s-ar potrivi, vă invităm să completați
        formularul de la secțiunea {0}.
      `,
    },
  },
}

export default new VueI18n({
  locale: 'ro',
  fallbackLocale: 'en',
  messages,
})
