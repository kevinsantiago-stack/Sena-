// Función tradicional
function saludar(nombre) {
return "Hola " + nombre;
}
// Función flecha equivalente
const saludarFlecha = (nombre) => {
return "Hola " + nombre;
}
// Función flecha ultra-corta (una línea)
const saludarCorta = nombre => "Hola " + nombre;
// Todas hacen lo mismo
console.log(saludar("Ana"));
// Hola Ana
console.log(saludarFlecha("Ana")); // Hola Ana
console.log(saludarCorta("Ana")); // Hola Ana

// Con arrays (muy útil)
let numeros = [1, 2, 3, 4, 5];
// Multiplicar cada número por 2
let dobles = numeros.map(n => n * 2);
console.log(dobles); // [2, 4, 6, 8, 10]
// Filtrar números pares
let pares = numeros.filter(n => n % 2 === 0);
console.log(pares); // [2, 4]
// Sumar todos los números
let suma = numeros.reduce((total, n) => total + n, 0);
console.log(suma); // 15