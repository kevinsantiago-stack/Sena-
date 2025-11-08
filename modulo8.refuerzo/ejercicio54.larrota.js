(function(){
let n = parseInt(prompt("Ingrese un número entero mayor que 1:"));
if (isNaN(n) || n<=1) { alert("Entrada inválida"); }
else {
  let prime = true;
  for(let i=2;i<=Math.sqrt(n);i++){ if(n%i===0){ prime=false; break; } }
  alert(prime ? "Es primo" : "No es primo");
}
})();