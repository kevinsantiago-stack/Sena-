class AutoLarrota {
  constructor(marcaLarrota, velocidadInicialLarrota) {
    this.marcaLarrota = marcaLarrota;
    this._velocidadLarrota = velocidadInicialLarrota;
  }

  set velocidadLarrota(valorLarrota) {
    if (valorLarrota >= 0) {
      this._velocidadLarrota = valorLarrota;
    } else {
      console.log("Error: Velocidad no puede ser negativa");
    }
  }

  get velocidadLarrota() {
    return this._velocidadLarrota;
  }
}


const carroLarrota = new AutoLarrota("Ford", 80);
console.log("Velocidad:", carroLarrota.velocidadLarrota);
carroLarrota.velocidadLarrota = 120; 
carroLarrota.velocidadLarrota = -50; 

//Getters y Setters: Beneficios

//Encapsulación
//El guion bajo (_velocidad) es
//una convención para indicar
//que la propiedad es "privada" y
//no debe accederse
//directamente.Getters y Setters: Beneficios

//Validación
//Los setters permiten validar
//datos antes de asignarlos,
//previniendo estados inválidos
//en tus objetos.

//Sintaxis Natural
//Se acceden como propiedades
//normales (carro.velocidad)
//aunque ejecutan funciones
//internamente.