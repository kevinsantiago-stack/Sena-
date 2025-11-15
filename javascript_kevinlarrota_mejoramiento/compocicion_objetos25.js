class LarrotaDireccion {
  constructor(larrotaCalle, larrotaCodigoPostal) {
    this.larrotaCalle = larrotaCalle;
    this.larrotaCodigoPostal = larrotaCodigoPostal;
  }
}

class LarrotaCliente {
  constructor(larrotaNombre, larrotaDireccion) {
    this.larrotaNombre = larrotaNombre;
    this.larrotaDireccion = larrotaDireccion;
  }

  mostrarLarrotaUbicacion() {
    console.log(`${this.larrotaNombre} vive en:
${this.larrotaDireccion.larrotaCalle},
CP ${this.larrotaDireccion.larrotaCodigoPostal}`);
  }
}

const larrotaDireccionInstancia = new LarrotaDireccion(
  "Calle de la Victoria 789", "11011"
);
const larrotaClienteInstancia = new LarrotaCliente("Larrota Gómez", larrotaDireccionInstancia);
larrotaClienteInstancia.mostrarLarrotaUbicacion();