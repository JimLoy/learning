const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  //entry: './src/index.js'  Default
  output:{ // Cambia el nombre de la carpeta de destino (en este caso)
    path: path.resolve(_dirname, 'build')
  },
  plugins:[//genera un html con el main.js ya inyectado
    new HtmlWebpackPlugin({template: 'src/index.html'})
  ],
  devServer:{//configurar el script 'dev' en el package.json
    open: true, //abre el navegador automaticamente
    port: 3000,
    overlay: true //muestra los errores en el navegador
  },
  module:{
    rules:[
      {
        test: /\.js$/, //webpack no entiende JSX por lo que se necesita un loader como Babel
        loader: 'babel-loader',
        options: { //opciones de configuracion para babel
          presets: [
            [
              '@babel/preset-react',
              {
                runtime: 'automatic' // Default es 'classic' (donde necesitas hacer import React from react)
              }
            ]
            ]
        }
      },
      {
        test:/\.css$/,
        use: ['style-loader', 'css-loader']
      }
    ]
  }
}
/*   https://www.youtube.com/watch?v=FMNuTj89RzU

    DEV DEPENDENCIAS

webpack
webpack-cli
webpack-dev-server
@babel/core
babel-loader
@babel/preset-react
style-loader
css-loader
html-webpack-plugin
*/