console.log("hola mundo");
console.log(32);
console.log("hola");
console.log(true);
console.log(false);


var saludo = "hola";
var respuesta = `Hola ${saludo}`

console.log(respuesta);

//-------------------------------------------------------------------//
var dias=1;
console.log((dias*24)*60*60);

//------------------------------------------------------------------//
//AREA DE UN RECTANGULO
var ancho=2;
var alto = 5;

var area = ancho*alto;

console.log(area);
//---------------------------------------------------------------------//
//Grados a Faherenheit
var grados = 20;
var Faherenheit = (9/5 * grados) + 32;
console.log(Faherenheit);

//---------------------------------------------------------------------//

var dia = "martES"

if (dia.toUpperCase() === 'LUNES') {
    console.log('MONDAY');
    
}else if(dia.toUpperCase() === 'MARTES'){
    console.log('TUESDAY');
}else if (dia.toUpperCase() === 'MIERCOELS') {
    console.log('WEDNESDAY');
}else if(dia.toUpperCase() === 'JUEVES'){
    console.log('THURSDAY');
} else if (dia.toUpperCase() === 'VIERNES') {
    console.log('FRIDAY');
}else if (dia.toUpperCase() === 'SABADO') {
    console.log('SATURDAY');
}else if (dia.toUpperCase() === 'DOMINGO') {
    console.log('SUNDAY');
}else {
    console.log('Ingrese un día la semana valido');
}

//----------------------------------------------------------------------//

switch (dia.toUpperCase()) {
    case 'LUNES':
        console.log('MONDAY');
        break;
    case 'MARTES':
        console.log('TUESDAY');
        break;
    case 'MIERCOLES':
        console.log('WEDNESDAY');
        break;
    case 'JUEVES':
        console.log('THURDAY');
        break;
    case 'VIERNES':
        console.log('FRIDAY');
        break;
    case 'SABADO':
        console.log('SATURDAY');
        break;
    case 'DOMINGO':
        console.log('SUNDAY');
    default:
        console.log('Ingrese un dia valido');
        break;
}

//------------------------------------------------------------------//


if (compras <= 10) {
    console.log(compras + 3);
} else if(compras > 10 && compras <= 20){
    console.log(compras + 5);
}else if (compras > 20 && compras <= 50 ) {
    console.log(compras + 7);
}else {
    console.log(`El envio es gratis:  ${compras}`);
}

var compras =51;
switch ((compras<=10 ? 1 : (compras <= 20 ? 2: (compras <= 50 ? 3 : (compras > 50 ? 4 : 0))))) {
    case 1:
        console.log(`Coste de envio $3:
        Total: ${compras + 3}`);
        break;
    case 2:
        console.log(`Coste de envio $5:
        Total: ${compras+5}`);
        break;
    case 3:
        console.log(`Coste de envio $7:
        Total: ${compras + 7}`);
        break
    case 4:
        console.log(`Coste de envio $0:
        Total: ${compras}`);
    default:
        break;
}

//----------------------------------------------------------------------------//

for (let i = 2; i < 13; i++) {
    console.log(`TABLA DEL ${i}`);
    for (let j = 0; j < 13; j++) {
        console.log(`${i} x ${j} = ${i*j}`);
    }
    console.log('\n');

}

i=2;

while (i<13) {

    console.log(`TABLA DEL ${i}`);
    j=0;
    while (j<13) {
        console.log(`${i} X ${j} = ${i*j}`);
        j++;
    }
    console.log('\n');
    i++;
}

/**
 * funciones
*/

function saludar(nombre) {
    console.log(`Hola como estas ${nombre}`);
}

saludar("Cristian")