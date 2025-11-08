(function(){
let n=parseInt(prompt("Sumar desde 1 hasta n, ingrese n:"));
if (isNaN(n) || n<1) { alert("Inválido"); }
else { let sum=0; for(let i=1;i<=n;i++) sum+=i; alert("Suma: " + sum); }
})();