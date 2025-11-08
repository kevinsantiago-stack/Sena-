(function(){
let edad = parseInt(prompt("Ingrese su edad:"));
if (isNaN(edad)) { alert("Por favor, ingrese una edad válida."); }
else { alert((edad >= 18) ? "Usted es mayor de edad." : "Usted es menor de edad."); }
})();