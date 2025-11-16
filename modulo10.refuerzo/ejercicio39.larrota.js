// Performance.now() - más preciso que Date
function medirTiempo(fn, nombre = "Función") {
let inicio = performance.now();
let resultado = fn();
let fin = performance.now();
let duracion = fin - inicio;
console.log(`${nombre} tomó ${duracion.toFixed(2)}ms`);
return resultado;
}
// Ejemplo de uso
function operacionLenta() {
let suma = 0;
for (let i = 0; i < 1000000; i++) {
suma += Math.random();
}
return suma;
}
medirTiempo(operacionLenta, "Operación con bucle");