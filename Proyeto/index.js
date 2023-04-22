const express = require('express');
const debug = require('debug')('app:main');
const app = express();
const{Config} = require('./src/Config'); 
const {ProductsAPI} = require('./src/Products');
const {USerAPI} = require('./src/Users');

const {IndexAPI,NotFoundAPI} = require('./src/index');

app.use(express.json());

IndexAPI(app);
ProductsAPI(app);
USerAPI(app);
NotFoundAPI(app);

//Modulos

app.listen(Config.port, ()=> {
    debug(`Servior escuchando en el puerto ${Config.port}`);
})