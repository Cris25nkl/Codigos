const express = require('express');
const {UserController} = require('./controller');
const router = express.Router();

module.exports.USerAPI = (app) =>{
    router
        .get('/', UserController.getUSers)
        .get('/:id', UserController.getUser)
        .post('/', UserController.createUSer);
        
    app.use('/api/user',router)
}