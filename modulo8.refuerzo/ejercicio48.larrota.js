(function(){
let numero = parseInt(prompt("Ingrese un número:"));
if (isNaN(numero)) { alert("Entrada inválida"); }
else { alert((numero % 2 === 0) ? ("El número " + numero + " es par.") : ("El número " + numero + " es impar.")); }
})();