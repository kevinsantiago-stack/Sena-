let frutas = ["manzana", "banana"];
let verduras = ["zanahoria", "brócoli"];
// Combinar arrays
let comida = [...frutas, ...verduras];
console.log(comida);
// ["manzana", "banana", "zanahoria", "brócoli"]
// Copiar array
let frutasCopia = [...frutas];
frutasCopia.push("naranja"); // No afecta el original
// Pasar como argumentos
function sumar(a, b, c) {
return a + b + c;
}
let numeros = [1, 2, 3];
console.log(sumar(...numeros)); // 6