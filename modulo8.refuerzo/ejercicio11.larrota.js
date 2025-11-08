(function(){
let y = parseInt(prompt("Ingrese un año:"));
if (isNaN(y)) { alert("Entrada inválida"); }
else { let es = ((y%4===0 && y%100!==0) || (y%400===0)) ? "Sí" : "No"; alert("¿Es bisiesto? " + es); }
})();