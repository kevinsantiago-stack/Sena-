const numeros = [1, 2, 3, 4, 5];

// Suma total
const suma = numeros.reduce((acumulador, actual) => acumulador + actual, 0);
console.log(suma); // 15

// Máximo
const maximo = numeros.reduce((max, actual) => actual > max ? actual : max, numeros[0]);
console.log(maximo); // 5