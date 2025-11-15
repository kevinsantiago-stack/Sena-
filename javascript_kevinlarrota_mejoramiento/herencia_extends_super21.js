class Auto {
  constructor(marcaLarrota, modeloLarrota) {
    this.marcaLarrota = marcaLarrota;
    this.modeloLarrota = modeloLarrota;
  }

  obtenerDescripcion() {
    return `Marca: ${this.marcaLarrota}, Modelo: ${this.modeloLarrota}`;
  }
}

class VehiculoElectrico extends Auto {
  constructor(marcaLarrota, modeloLarrota, autonomiaLarrota) {
    super(marcaLarrota, modeloLarrota);
    this.autonomiaBateriaLarrota = autonomiaLarrota;
  }

  mostrarInfo() {
    return `${super.obtenerDescripcion()}, Autonomía: ${this.autonomiaBateriaLarrota} km`;
  }
}

const teslaLarrota = new VehiculoElectrico("Tesla", "Model 3", 500);
console.log(teslaLarrota.mostrarInfo());