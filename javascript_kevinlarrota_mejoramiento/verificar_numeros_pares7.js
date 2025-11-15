
function verificarParImpar(numero) {
 if (numero % 2 === 0) {
 console.log(numero + " es par");
 } else {
 console.log(numero + " es impar");
 }
}
// Pruebas

verificarParImpar(15); // "15 es impar"
verificarParImpar(20); // "20 es par"
verificarParImpar(0); // "0 es par"
verificarParImpar(-3); // "-3 es impar"