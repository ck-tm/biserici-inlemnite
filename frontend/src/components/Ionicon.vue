<template>
  <component :is="icon[1]" />
</template>

<script>
const components = {}
const componentList = {
  Add: 'ios-add',
  ArrowBack: 'ios-arrow-back',
  ArrowDown: 'ios-arrow-down',
  ArrowForward: 'ios-arrow-forward',
  // ArrowDropright: 'md-arrow-dropright',
  Alert: 'md-alert',
  Burger: 'md-menu',
  Close: 'md-close',
  Cube: 'md-cube',
  Images: 'md-images',
  Options: 'md-options',
  People: 'md-people',
  Person: 'md-person',
  Search: 'md-search',
  Trash: 'md-trash',
  Warning: 'ios-warning',
}

for (let key in componentList) {
  components[key] = () => import(`vue-ionicons/dist/${componentList[key]}.vue`)
}

export default {
  name: 'Ionicon',
  components,
  props: {
    icon: Array,
    size: String,
  },
}
</script>
