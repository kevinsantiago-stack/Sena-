(function(){
let n = parseInt(prompt("Número decimal:"));
if (isNaN(n)) { alert("Inválido"); }
else { alert("Binario: " + n.toString(2)); }
})();