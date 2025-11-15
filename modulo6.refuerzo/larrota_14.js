class larrota {
  constructor(nombre) {
    this.nombre = nombre;
  }

  saludar() {
    console.log("Hola " + this.nombre);
  }
}

let persona = new larrota("Kevin");
persona.saludar();
