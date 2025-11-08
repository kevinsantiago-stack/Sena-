(function(){
let n = prompt("Ingrese un número entero:");
if (!/^-?\d+$/.test(n)) { alert("Entrada inválida"); }
else { let s = n.replace('-','').split('').reduce((a,c)=>a+parseInt(c),0); alert("Suma de dígitos: " + s); }
})();