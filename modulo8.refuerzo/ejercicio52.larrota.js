(function(){
let precio = parseFloat(prompt("Precio:"));
let descuento = parseFloat(prompt("Descuento %:"));
if (isNaN(precio) || isNaN(descuento)) { alert("Entrada inválida"); }
else { let final = precio * (1 - descuento/100); alert("Precio final: " + final.toFixed(2)); }
})();