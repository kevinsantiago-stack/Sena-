(function(){
let filas=parseInt(prompt("Número de filas:"));
if (isNaN(filas) || filas<1) { alert("Inválido"); }
else { let s=""; for(let i=1;i<=filas;i++){ s += "*".repeat(i) + "\n"; } alert(s); }
})();