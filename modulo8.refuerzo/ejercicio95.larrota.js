(function(){
let e = prompt("Ingrese email:");
if (!e) { alert("Vacío"); }
else { alert( (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e)) ? "Válido" : "Inválido"); }
})();