/*
const saludo = require("./saludo.js");

console.log(saludo.saludar("Cristian"));
console.log(saludo.saludo2());


//solo usar una funcion

const { saludo2, saludar } = require('./saludo.js');

console.log(saludo2())
console.log(saludar())


console.warn('ERROR')
console.error('Muchos errores')

console.error(new Error('Muchos errores'))

//Usos de Process
console.log(process.argv);
console.log(process.memoryUsage());


//Uso de os

const os = require ('os');

console.log(os.type())
console.log(os.homedir())
console.log(os.uptime())
console.log(os.userInfo())
*/

//Uso de Timer

function mostrar (tema){
  console.log(`mostrar ${tema}`);
}

setTimeout(mostrar, 2000, 'La cara');
