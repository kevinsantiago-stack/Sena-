// Guardar texto simple
localStorage.setItem("nombre", "María");
1
// Guardar números
localStorage.setItem("edad", "25");
// Guardar objetos (convertir a JSON)
let usuario = {
nombre: "Juan",
preferencias: ["azul", "grande"]
};
localStorage.setItem("usuario", JSON.stringify(usuario));

//Recuperar Información
// Leer texto
let nombreGuardado = localStorage.getItem("nombre");
console.log(nombreGuardado); // "María"
2
// Leer y convertir a número
let edadGuardada = parseInt(localStorage.getItem("edad"));
// Leer objetos (convertir de JSON)
let usuarioGuardado = JSON.parse(localStorage.getItem("usuario"));
console.log(usuarioGuardado.nombre); // "Juan"


//Limpiar Storage
// Eliminar un elemento específico
localStorage.removeItem("nombre");
3
// Eliminar todo
localStorage.clear();
// Verificar si existe
if (localStorage.getItem("usuario")) {
console.log("Usuario existe");
}