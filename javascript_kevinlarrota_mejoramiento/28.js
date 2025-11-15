class LarrotaAuto {
  constructor(larrotaMarca, larrotaModelo) {
    this.larrotaMarca = larrotaMarca;
    this.larrotaModelo = larrotaModelo;
  }

  obtenerLarrotaDescripcion() {
    return `${this.larrotaMarca} ${this.larrotaModelo}`;
  }
}

export default LarrotaAuto;