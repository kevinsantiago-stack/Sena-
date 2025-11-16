// Este código se ejecuta en un hilo separado
self.addEventListener('message', function(e) {
let {comando, datos} = e.data;
if (comando === 'calcular_factorial') {
let resultado = calcularFactorial(datos);
// Enviar resultado de vuelta
self.postMessage({
comando: 'factorial_completo',
resultado: resultado
});
}
});
function calcularFactorial(n) {
console.log(`Worker: Calculando factorial de ${n}`);
if (n <= 1) return 1;
let resultado = 1;
for (let i = 2; i <= n; i++) {
resultado *= i;
}
return resultado;
}