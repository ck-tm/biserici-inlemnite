import { extend, localize, setInteractionMode } from 'vee-validate'

import { required, email, min } from 'vee-validate/dist/rules'

import ro from './locale/ro.json'
import en from './locale/en.json'

const rules = { required, email, min }

Object.keys(rules).forEach((rule) => {
  extend(rule, rules[rule])
})

localize({ ro, en })
localize('ro')

setInteractionMode('eager')
