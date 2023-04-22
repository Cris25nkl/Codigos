function saludar(nombre){
    return `Hola ${nombre}`
}

function saludo2(){
    return 'Hola mundo'
}
/*module.exports.saludar = saludar;
module.exports.saludo2 = saludo2;
//exportar varios
*/
module.exports = {  
    saludar: saludar,
    saludo2: saludo2
};