(function(){
let n = parseFloat(prompt("Ingrese un número:"));
if (isNaN(n)) { alert("Entrada inválida"); }
else { alert((n>0)?"positivo":(n<0)?"negativo":"cero"); }
})();