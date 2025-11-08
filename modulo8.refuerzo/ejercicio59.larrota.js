(function(){
let capital = parseFloat(prompt("Capital:"));
let tasa = parseFloat(prompt("Tasa anual %:"));
let tiempo = parseFloat(prompt("Tiempo (años):"));
if (isNaN(capital)||isNaN(tasa)||isNaN(tiempo)) { alert("Entrada inválida"); }
else { let interes = capital * (tasa/100) * tiempo; alert("Interés simple: " + interes.toFixed(2)); }
})();