var BundleTracker = require('webpack-bundle-tracker')
var WriteFilePlugin = require('write-file-webpack-plugin')


module.exports = {
  outputDir: (process.env.NODE_ENV === "production" ? 'dist' : 'static'),
  baseUrl: '/',

 devServer: {
    publicPath: "http://localhost:8080/",
    headers: {
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, PATCH, OPTIONS",
      "Access-Control-Allow-Headers": "Origin, X-Requested-With, Content-Type, Accept, Accept-Encoding, Accept-Language, Access-Control-Request-Headers, Access-Control-Request-Method",
      "Access-Control-Allow-Credentials": "true"
    }
  },

  chainWebpack: config => {
    config.optimization.splitChunks({
      cacheGroups: {
        vendors: {
          name: 'chunk-vendors',
          test: /[\\\/]node_modules[\\\\/]/,
          priority: -10,
          chunks: 'initial'
        },
        common: {
          name: 'chunk-common',
          minChunks: 2,
          priority: -20,
          chunks: 'initial',
          reuseExistingChunk: true
        }
      }
    })
  },
  configureWebpack: {
    output: {
      filename: 'js/[name].js',
      chunkFilename: 'js/[name].js'
    },
    plugins: [
      new WriteFilePlugin(),
      (process.env.NODE_ENV === "production" ?
        new BundleTracker({
          filename: 'webpack-stats-prod.json',
          publicPath: '/'
        }) :
        new BundleTracker({
          filename: 'webpack-stats.json',
          publicPath: 'http://localhost:8080/'
        })
      )
    ]
  }
}