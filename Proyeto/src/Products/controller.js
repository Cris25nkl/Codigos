const createError = require('http-errors');
const debug = require('debug')('app:module-products-controller');
const {ProductsService} = require('./services');

const{ Response } = require('../Common/response');

module.exports.ProductsController = {
    getProducts: async (req,res)=> {
        try {
            let products = await ProductsService.getAll();
            Response.success(res,200,'Lista de productos',products)
        } catch (error) {
            debug(error)
            Response.error(res)
            
        }
    },
    getProduct: async(req,res)=> {
        try {
            const {params: {id}} = req;
            let product = await ProductsService.getById(id);
            if (!product) {
                Response.error(res, new createError.NotFound())
            }else{
                Response.success(res,200,`Producto ${id}`,product)
            }
            
        } catch (error) {
            debug(error)
            Response.error(res)
        }
    },



    createProducts: async (req,res)=> {
        try {
            debug('Entra')
            const {body} = req;

            if (!body || Object.keys(body).length === 0) {
                debug('entra2')
                Response.error(res, new createError.BadRequest())
            }else{
                debug('entra3')
                const insertedID = await ProductsService.create(body);
                Response.success(res,201,'Producto agregado', insertedID);
            }
        } catch (error) {
            debug('entra4')
            debug(error)
            Response.error(res)
        }
    },

    generateReport: (req, res) => {
        try {
            ProductsService.generateReport('Inventario',res)
        } catch (error) {
            debug(error)
            Response.error(res)
        }
    }
}