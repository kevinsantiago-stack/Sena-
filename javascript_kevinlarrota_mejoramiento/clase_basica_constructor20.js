class AutoLarrota {
  constructor(cuervoMarca, cuervoModelo) {
    this.cuervoMarca = cuervoMarca;
    this.cuervoModelo = cuervoModelo;
  }

  obtenerDescripcionLarrota() {
    return `Marca: ${this.cuervoMarca}, Modelo: ${this.cuervoModelo}`;
  }
}

const miLarrotaAuto = new AutoLarrota("Toyota", "Corolla");
console.log(miLarrotaAuto.obtenerDescripcionLarrota());

export default AutoLarrota;

// TIP: Las clases permiten encapsular propiedades y métodos para representar objetos con comportamiento.