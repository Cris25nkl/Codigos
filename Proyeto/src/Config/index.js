require('dotenv').config();

module.exports.Config ={
    port: process.env.PORT,
    mongouri: process.env.MONGO_URI,
    mongoName: process.env.MONGO_NAME,
}