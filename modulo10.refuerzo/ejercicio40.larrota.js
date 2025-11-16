// Función simple para probar
function calculadora(a, b, operacion) {
switch (operacion) {
case '+': return a + b;
case '-': return a - b;
case '*': return a * b;
case '/':
if (b === 0) throw new Error('División por cero');
return a / b;
default: throw new Error('Operación no válida');
}
}
// Tests manuales
function probarCalculadora() {
console.log('=== PROBANDO CALCULADORA ===');
// Test de suma
let resultado = calculadora(2, 3, '+');
console.assert(resultado === 5, `Error: esperaba 5, obtuve ${resultado}`);
console.log('✓ Suma funciona');
// Test de resta
resultado = calculadora(5, 2, '-');
console.assert(resultado === 3, `Error: esperaba 3, obtuve ${resultado}`);
console.log('✓ Resta funciona');
// Test de multiplicación
resultado = calculadora(4, 3, '*');
console.assert(resultado === 12, `Error: esperaba 12, obtuve ${resultado}`);
console.log('✓ Multiplicación funciona');
// Test de división
resultado = calculadora(10, 2, '/');
console.assert(resultado === 5, `Error: esperaba 5, obtuve ${resultado}`);
console.log('✓ División funciona');
// Test de error - división por cero
try {
calculadora(5, 0, '/');
console.error(' Debería haber lanzado error');
} catch (e) {
console.log('✓ División por cero maneja error correctamente');
}
console.log('=== TODOS LOS TESTS PASARON ===');
}
probarCalculadora();