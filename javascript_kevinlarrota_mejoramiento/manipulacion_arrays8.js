// ejercicio08.js
let pilaLibros = ["El Quijote", "100 Años de Soledad", "Fahrenheit 451"];
console.log("Libros iniciales:", pilaLibros.length); // 3
// Agregar al final
pilaLibros.push("Moby Dick");
console.log("Después de push:", pilaLibros.length); // 4
console.log("Libros:", pilaLibros);
// Remover del final
let libroEliminado = pilaLibros.pop();
console.log("Libro removido:", libroEliminado); // "Moby Dick"
console.log("Libros finales:", pilaLibros.length); // 3