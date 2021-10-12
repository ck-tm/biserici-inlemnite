// const path = require('path')

module.exports = {
  filenameHashing: process.env.NODE_ENV === 'production',
  productionSourceMap: false,

  pluginOptions: {
    'style-resources-loader': {
      preProcessor: 'scss',
      patterns: [
        '/Users/kenji/code/ck/biserici-inlemnite/frontend/src/assets/style/variables.scss',
      ],
    },
  },
}
