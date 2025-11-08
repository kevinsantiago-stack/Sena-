(function(){
let n=parseInt(prompt("Número para tabla:"));
if (isNaN(n)) { alert("Inválido"); }
else { let s=""; for(let i=1;i<=10;i++){ s += n + " x " + i + " = " + (n*i) + "\n"; } alert(s); }
})();