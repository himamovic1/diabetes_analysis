"use strict";

/*
 * Plugins
 */
const webpack = require('webpack');
const path = require("path");
const CleanWebpackPlugin = require('clean-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const ManifestRevisionPlugin = require('manifest-revision-webpack-plugin');

/*
 * Target names
 */
const libraryName = 'app';
const filename_js = '[name].[hash].js';
const chunkFilename_js = '[id].[hash].js';
const filename_css = '[name].[hash].css';

/*
 * Paths
 */
const contextRoot = path.join(__dirname, '..');
const staticDir = path.join(contextRoot, 'bss_diabetes', 'static');
const manifestPath = path.join(contextRoot, 'webpack', 'manifest.json');

const rootAssetPath = path.join(staticDir, 'source');
const sourceDir = path.join(staticDir, 'bundles');
const outputDir = path.join(staticDir, 'build');

const scriptBundle = [
    path.join(sourceDir, 'main.js')
];

const styleBundle = [
    path.join(sourceDir, 'main.scss')
];


/*
 * Configuration
 */
module.exports = {
    context: contextRoot,
    target: 'web',
    entry: {
        main_js: scriptBundle,
        main_css: styleBundle
    },
    output: {
        path: outputDir,
        filename: filename_js,
        chunkFilename: chunkFilename_js,
        library: libraryName,
        libraryTarget: 'umd',
        umdNamedDefine: true
    },
    resolve: {
        extensions: ['.js', '.jsx', '.css', '.scss'],
        modules: ["node_modules"]
    },
    devtool: 'source-map',
    devServer: {
        headers: {'Access-Control-Allow-Origin': '*'}
    },
    module: {
        loaders: [
            {
                test: /\.js?$/,
                loader: 'babel-loader',
                exclude: /node_modules/
            },
            {
                test: /\.html$/,
                loader: 'raw-loader'
            },
            {
                test: /\.scss$/,
                loader: ExtractTextPlugin.extract({
                    fallback: 'style-loader',
                    use: 'css-loader!sass-loader'
                })
            },
            {
                test: /\.css$/,
                loader: ExtractTextPlugin.extract({
                    fallback: 'style-loader',
                    use: 'css-loader'
                })
            },
            {
                test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/,
                loader: 'url-loader?limit=10000&mimetype=application/font-woff'
            },
            {
                test: /\.(ttf|eot|svg|png|jpe?g|gif|ico)(\?.*)?$/i,
                loader: 'file-loader?context=' + rootAssetPath + '&name=[path][name].[hash].[ext]'
            }
        ]
    },
    plugins: [
        new ExtractTextPlugin(filename_css),
        new CleanWebpackPlugin(
            [outputDir],
            {
                root: contextRoot,
                verbose: true,
                dry: false,
                exclude: ['script.js', 'style.css']
            }
        ),
        new ManifestRevisionPlugin(manifestPath, {
            rootAssetPath: rootAssetPath,
            ignorePaths: [
                'css', 'scss', 'js', 'bundles', 'plugins',
                '.scss', '.less', '.css', '.js', '.db', '.otf'
            ]
        })
    ]
};