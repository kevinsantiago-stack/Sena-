function Estudiante(nombre, edad, carrera) {
  Persona.call(this, nombre, edad); 
  this.carrera = carrera;
}

Estudiante.prototype = Object.create(Persona.prototype);
Estudiante.prototype.constructor = Estudiante;

Estudiante.prototype.estudiar = function() {
  return `${this.nombre} está estudiando ${this.carrera}`;
};

const carlos = new Estudiante("Carlos", 20, "Ingeniería");
console.log(carlos.saludar());   
console.log(carlos.estudiar()); 