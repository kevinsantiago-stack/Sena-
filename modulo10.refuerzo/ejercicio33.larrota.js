// Función generator (nota el asterisco)
function* contarHasta(limite) {
let i = 1;
while (i <= limite) {
yield i; // Pausa y devuelve valor
i++;
}
return "¡Terminado!";
}
// Usar el generator
let contador = contarHasta(3);
console.log(contador.next()); // {value: 1, done: false}
console.log(contador.next()); // {value: 2, done: false}
console.log(contador.next()); // {value: 3, done: false}
console.log(contador.next()); // {value: "¡Terminado!",
done: true
