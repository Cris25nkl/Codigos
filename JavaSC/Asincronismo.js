/**
 * Uso de los time set para multi tareas
console.log("Tarea 1");
console.log("Tarea 2");
console.log("Tarea 3");
setTimeout(() => {
    console.log("Tarea 4");
}, 2000);

console.log("Tarea 5");
*/

/**
 * Callback
 */

const suma = (a, b, cb) => {
    cb (a + b)
}

const imprimir = (data) => console.log(data);


/**var resultado = suma(1,2,(resultado) => {
    console.log(resultado);
})*/

var resultado = suma(1,2,imprimir)

const getdata = (cb,cbError) => {
    if (true) {
        
    setTimeout(() => {
        cb({
            nombre: "Cristian",
            apellido: "Florez"
        })
    }, 3000);
   
    }else{
        cbError(new Error("No hay informacion"))
    }
};

const errorhandler = (error) => console.log(error);
const imprimirdata = (data) => console.log(data);

getdata(imprimirdata,errorhandler);
/*********************************************************** */

/**
 * Promesas o promises
 */

const getData1 = (error) => new Promise((resolve,reject) => {
    if (!error) {
        setTimeout(() => {
            resolve({
                nombre:"aniel",
                apellio:"Fuentes"
            })
        }, 3000);
        
    }else {
        reject("No hay datos")
    }
})
console.log("inicio");
getData1(false).then((data)=>{
    console.log(data);
}).catch((error)=>{
    console.log(error);
})
console.log("fin");
const getData2 = new Promise((resolve,reject)=>{})


/**
 * Async-await
 */

const main = async () =>{
    try {
        let resultado = await getData1(false)
        console.log(resultado);  
    } catch (error) {
        console.log(error);
    }
    
}
main()