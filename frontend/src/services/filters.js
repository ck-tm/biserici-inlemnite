import Vue from 'vue'
import { BooleanOptions } from '@/services/utils'

Vue.filter('formatFieldValue', function (value) {
  if (typeof value == 'boolean') return BooleanOptions[value.toString()]

  return value
})
