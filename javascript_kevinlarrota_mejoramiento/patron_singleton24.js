class AutoLarrota {
  constructor(marcaLarrota, velocidadInicialLarrota) {
    this.marcaLarrota = marcaLarrota;
    this._velocidadLarrota = velocidadInicialLarrota;
  }

  set velocidad(valor) {
    if (valor >= 0) {
      this._velocidadLarrota = valor;
    } else {
      console.log("Error: Velocidad no puede ser negativa");
    }
  }

  get velocidad() {
    return this._velocidadLarrota;
  }
}

const carroLarrota = new AutoLarrota("Ford", 80);

console.log("Velocidad:", carroLarrota.velocidad);
carroLarrota.velocidad = 120;
console.log("Velocidad actualizada:", carroLarrota.velocidad);
carroLarrota.velocidad = -50;