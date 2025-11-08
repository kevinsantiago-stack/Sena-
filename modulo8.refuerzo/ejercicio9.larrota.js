(function(){
let total = parseFloat(prompt("Cuenta total:"));
let porcentaje = parseFloat(prompt("Porcentaje de propina (ej. 15):"));
if (isNaN(total) || isNaN(porcentaje)) { alert("Entrada inválida"); }
else { let propina = total * (porcentaje/100); alert("Propina: " + propina.toFixed(2) + "\nTotal: " + (total+propina).toFixed(2)); }
})();