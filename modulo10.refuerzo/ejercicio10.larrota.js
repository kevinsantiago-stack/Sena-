let persona = {
nombre: "Ana",
edad: 28,
profesion: "Doctora",
esActiva: true
};
console.log(persona.nombre); // "Ana"
console.log(persona["edad"]); // 28

// Cambiar valores existentes
persona.edad = 29;
// Agregar nuevas propiedades
persona.ciudad = "Madrid";
// Eliminar propiedades
delete persona.esActiva;