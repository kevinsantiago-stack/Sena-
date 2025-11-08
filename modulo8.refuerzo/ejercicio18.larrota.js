(function(){
let distancia = parseFloat(prompt("Distancia (m):"));
let tiempo = parseFloat(prompt("Tiempo (s):"));
if (isNaN(distancia) || isNaN(tiempo) || tiempo===0) { alert("Entrada inválida"); }
else { alert("Velocidad: " + (distancia/tiempo).toFixed(2) + " m/s"); }
})();