let boton = document.getElementById("miBoton");
// Click simple
boton.addEventListener("click", function() {
alert("¡Click!");
});
// Doble click
boton.addEventListener("dblclick", function() {
console.log("¡Doble click!");
});
// Mouse sobre el elemento
boton.addEventListener("mouseenter", function() {
boton.style.backgroundColor = "yellow";
});


let input = document.getElementById("miInput");
// Tecla presionada
input.addEventListener("keydown", function(evento) {
console.log("Tecla presionada:", evento.key);
});
// Al escribir en el input
input.addEventListener("input", function() {
console.log("Valor actual:", input.value);
});


//Eventos de Formulario
let formulario = document.getElementById("miForm");
formulario.addEventListener("submit", function(evento)
{
evento.preventDefault(); // Evitar envío automático
let nombre =
document.getElementById("nombre").value;
alert("Hola, " + nombre + "!");
});