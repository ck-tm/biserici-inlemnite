import Vue from 'vue'

import {
  Button,
  Checkbox,
  Dropdown,
  Field,
  Icon,
  Input,
  Loading,
  Radio,
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
Vue.use(Dropdown)
Vue.use(Field)
Vue.use(Icon)
Vue.use(Input)
Vue.use(Loading)
Vue.use(Radio)
Vue.use(Tabs)
Vue.use(Toast)
