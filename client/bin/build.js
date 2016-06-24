#!/usr/bin/env node
require('../server.babel'); // babel registration (runtime transpilation for node)
var fs=require('fs-extra');
var path = require('path');
var rootDir = path.resolve(__dirname, '..');
const basedir = process.cwd();

/**
 * Define isomorphic constants.
 */
global.__CLIENT__ = false;
global.__SERVER__ = true;
global.__DISABLE_SSR__ = false;  // <----- DISABLES SERVER SIDE RENDERING FOR ERROR DEBUGGING
global.__DEVELOPMENT__ = process.env.NODE_ENV !== 'production';

// https://github.com/halt-hammerzeit/webpack-isomorphic-tools
var WebpackIsomorphicTools = require('webpack-isomorphic-tools');
global.webpackIsomorphicTools = new WebpackIsomorphicTools(require('../webpack/webpack-isomorphic-tools'))
  .development(__DEVELOPMENT__)
  .server(rootDir, function() {

  fs.readFile(basedir + '/src/index.html', 'utf8', function done(err, data) {
    const html = data.replace(`<script src="client.js"></script>`, `<script src="${webpackIsomorphicTools.assets().javascript.main}"></script>`)
    .replace(`href="styles.css">`, `href="${webpackIsomorphicTools.assets().styles.main}">`);
    fs.outputFile(basedir + '/index.html', html);
    console.log(`copied 'index.html'.`);
  });
});

