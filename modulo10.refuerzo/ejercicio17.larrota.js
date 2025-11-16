try {
// Código que podría fallar
let resultado = 10 / 0;
console.log(resultado);
} catch (error) {
// Qué hacer si hay error
console.log("Ocurrió un error:", error.message);
} finally {
// Código que siempre se ejecuta
console.log("Proceso terminado");
}

function dividir(a, b) {
if (b === 0) {
throw new Error("No se puede dividir por cero");
}
return a / b;
}
try {
console.log(dividir(10, 2)); // 5
console.log(dividir(10, 0)); // ¡Error!
} catch (error) {
alert("Error: " + error.message);
}