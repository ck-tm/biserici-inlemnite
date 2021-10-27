import Vue from 'vue'

import {
  Button,
  Checkbox,
  Carousel,
  Collapse,
  Dropdown,
  Field,
  Icon,
  Input,
  Loading,
  Modal,
  Radio,
  Table,
  Tabs,
  Toast,
  ConfigProgrammatic,
} from 'buefy'

ConfigProgrammatic.setOptions({
  defaultTrapFocus: true,
  defaultIconComponent: 'Ionicon',

  customIconPacks: {
    mdi: {
      iconPrefix: '',
      internalIcons: {
        'alert-circle': 'alert',
        'chevron-left': 'arrow-back',
        'chevron-right': 'arrow-forward',
      },
    },
  },

  defaultNoticeQueue: false,
  defaultToastDuration: 3000,
  // defaultToastPosition: 'is-bottom',
  defaultInputHasCounter: false,
  defaultUseHtml5Validation: false,
  defaultDialogConfirmText: 'Confirmă',
  defaultDialogCancelText: 'Anulează',
  // defaultModalCanCancel: false,
})

// Components
Vue.use(Button)
Vue.use(Checkbox)
Vue.use(Carousel)
Vue.use(Collapse)
Vue.use(Dropdown)
Vue.use(Field)
Vue.use(Icon)
Vue.use(Input)
Vue.use(Loading)
Vue.use(Modal)
Vue.use(Radio)
Vue.use(Table)
Vue.use(Tabs)
Vue.use(Toast)
