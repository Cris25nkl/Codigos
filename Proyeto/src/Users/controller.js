const createError = require('http-errors');
const debug = require('debug')('app:module-user-controller');
const {USerService} = require('./services');

const{ Response } = require('../Common/response');

module.exports.UserController = {
    getUSers: async (req,res)=> {
        try {
            let users = await USerService.getAll();
            Response.success(res,200,'Lista de usuarios',users)
        } catch (error) {
            debug(error)
            Response.error(res)
            
        }
    },
    getUser: async(req,res)=> {
        try {
            const {params: {id}} = req;
            let user = await USerService.getById(id);
            if (!user) {
                Response.error(res, new createError.NotFound())
            }else{
                Response.success(res,200,`Usuario ${id}`,user)
            }
            
        } catch (error) {
            debug(error)
            Response.error(res)
        }
    },



    createUSer: async (req,res)=> {
        try {
            debug('Entra')
            const {body} = req;

            if (!body || Object.keys(body).length === 0) {
                debug('entra2')
                Response.error(res, new createError.BadRequest())
            }else{
                debug('entra3')
                const insertedID = await USerService.create(body);
                Response.success(res,201,'Usuario agregado', insertedID);
            }
        } catch (error) {
            debug('entra4')
            debug(error)
            Response.error(res)
        }
    },


}