"use strict";

/*
 * Plugins and loaders
 */
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');
const WebpackStripLoader = require('strip-loader');
let devConfig = require('./config.dev.js');

let prodLoaders = [
    {
        test: [/\.js$/, /\.es6$/],
        exclude: /node_modules/,
        loader: WebpackStripLoader.loader('console.log', 'alert')
    }
];

let prodPlugins = [
    new UglifyJSPlugin({
        sourceMap: false,
        compress: {
            sequences: true,
            dead_code: true,
            conditionals: true,
            booleans: true,
            unused: true,
            if_return: true,
            join_vars: true,
            drop_console: true
        },
        mangle: {
            except: ['$super', '$', 'exports', 'require']
        },
        output: {
            comments: false
        }
    }),
    new OptimizeCssAssetsPlugin({
        assetNameRegExp: /\.css$/,
        cssProcessor: require('cssnano'),
        cssProcessorOptions: {discardComments: {removeAll: true}},
        canPrint: true
    }),
];


/*
 * Extending dev config
 */
Array.prototype.push.apply(devConfig.module.loaders, prodLoaders);
Array.prototype.push.apply(devConfig.plugins, prodPlugins);

module.exports = devConfig;