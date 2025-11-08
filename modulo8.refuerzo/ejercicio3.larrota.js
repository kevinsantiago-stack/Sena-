(function(){
let a = parseFloat(prompt("Ingrese el primer número:"));
let b = parseFloat(prompt("Ingrese el segundo número:"));
let c = parseFloat(prompt("Ingrese el tercer número:"));
if ([a,b,c].some(isNaN)) { alert("Entrada inválida"); }
else { let m = Math.max(a,b,c); alert("El mayor es: " + m); }
})();