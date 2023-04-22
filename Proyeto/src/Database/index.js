const {MongoClient} = require('mongodb');
const debug = require('debug')('app:module-database');
const { Config } = require('../Config');

var connection = null;
module.exports.Database = (collection) => new Promise ( async (res,rej)=>{
    try {
        if (!connection) {
            const client = new MongoClient(Config.mongouri);
            connection = await client.connect();
            debug('Nueva conexion realizada')
        }
        debug('Reutilizando conexion')
        const db = connection.db(Config.mongoName);
        res(db.collection(collection))
        
    } catch (error) {
        rej(error);
    }
})