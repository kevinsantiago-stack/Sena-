// ejercicio09.js
function sumarArreglo(arr) {
 let suma = 0;
 for (let i = 0; i < arr.length; i++) {
 suma += arr[i];
 }
 return suma;
}
let ventas = [100, 200, 300, 400, 500];
console.log("Total:", sumarArreglo(ventas));
// Salida: 1500


//Anatomía del Bucle for
//Inicialización: let i = 0
// Comienza en el índice 0
//Condición: i < arr.length
//Continúa mientras i sea menor que la longitud
//Incremento: i++
//Aumenta i después de cada iteración
//Acumulador: suma += arr[i]
//Va sumando cada elemento