// Definimos la clase Auto
class Auto {
  constructor(marca, modelo, año) {
    this.marca = marca;
    this.modelo = modelo;
    this.año = año;
    this.encendido = false;
  }

  encender() {
    this.encendido = true;
    console.log(`${this.marca} ${this.modelo} está encendido.`);
  }

  apagar() {
    this.encendido = false;
    console.log(`${this.marca} ${this.modelo} está apagado.`);
  }

  info() {
    return `Auto: ${this.marca} ${this.modelo} (${this.año})`;
  }
}

// Creamos una instancia de Auto
const miAuto = new Auto("Toyota", "Corolla", 2020);

// Usamos los métodos del objeto
console.log(miAuto.info());     // Auto: Toyota Corolla (2020)
miAuto.encender();              // Toyota Corolla está encendido.
miAuto.apagar();                // Toyota Corolla está apagado.