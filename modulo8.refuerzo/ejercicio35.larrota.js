(function(){
let n = parseInt(prompt("Ingrese un entero no negativo:"));
if (isNaN(n) || n<0) { alert("Entrada inválida"); }
else { let f=1; for(let i=2;i<=n;i++) f*=i; alert("Factorial: " + f); }
})();