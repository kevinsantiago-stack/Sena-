// Crear array
let frutas = ["manzana", "banana", "naranja"];
// Acceder a elementos (empieza en 0)
console.log(frutas[0]); // "manzana"
console.log(frutas[1]); // "banana"
// Cambiar elementos
frutas[1] = "pera";
console.log(frutas); // ["manzana", "pera", "naranja"]

let numeros = [1, 2, 3];
// Agregar al final
numeros.push(4);
console.log(numeros); // [1, 2, 3, 4]
// Quitar el último
let ultimo = numeros.pop();
console.log(ultimo); // 4
console.log(numeros); // [1, 2, 3]
// Longitud del array
console.log(numeros.length); // 3