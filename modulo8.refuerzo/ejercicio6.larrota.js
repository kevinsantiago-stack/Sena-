(function(){
let limite = parseInt(prompt("Ingrese un número para contar hasta él:"));
if (isNaN(limite) || limite <= 0) { alert("Número inválido"); }
else { let msg=""; for(let i=1;i<=limite;i++){ msg += i + "\n"; } alert(msg); }
})();