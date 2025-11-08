(function(){
let temperatura = parseFloat(prompt("Ingrese la temperatura:"));
let tipo = prompt("Convertir a Fahrenheit (F) o Celsius (C)?").toUpperCase();
if (isNaN(temperatura)) { alert("Entrada inválida"); }
else if (tipo === 'F') { alert(temperatura + "°C es " + ((temperatura * 9/5) + 32).toFixed(2) + "°F"); }
else if (tipo === 'C') { alert(temperatura + "°F es " + (((temperatura - 32) * 5/9)).toFixed(2) + "°C"); }
else { alert("Tipo inválido"); }
})();