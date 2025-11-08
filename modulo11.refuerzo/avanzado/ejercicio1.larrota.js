function Persona(nombre, edad) {
  this.nombre = nombre;
  this.edad = edad;
}

Persona.prototype.saludar = function() {
  return `Hola, soy ${this.nombre} y tengo ${this.edad} años`;
};

Persona.prototype.esMayorDeEdad = function() {
  return this.edad >= 18;
};

const ana = new Persona("Ana", 25);
console.log(ana.saludar());          
console.log(ana.esMayorDeEdad());    