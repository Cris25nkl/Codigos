const { ObjectId } = require('mongodb');

const {ProductsUtils} = require('./utils');
const {Database} = require('../Database');
const COLLECTION = 'products'
const getAll=async ()=>{
    const collection = await Database(COLLECTION);
    return await collection.find({}).toArray();
}

const getById = async(id) => {
    const collection = await Database(COLLECTION);
    return collection.findOne({_id: new ObjectId(id)})
}


const create = async (product) =>{
    const collection = await Database(COLLECTION);
    let result = await collection.insertOne(product);
    return result.insertedID;
}

const generateReport = async(name,res)=>{
    let products =await getAll()
    ProductsUtils.exelGenerator(products,name,res)
} 
module.exports.ProductsService = {
    getAll,getById,create,generateReport
}