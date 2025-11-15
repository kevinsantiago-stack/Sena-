class AutoLarrota {
  constructor(marcaLarrota, modeloLarrota) {
    this.marcaLarrota = marcaLarrota;
    this.modeloLarrota = modeloLarrota;
  }

  static informacionGeneralLarrota() {
    return "Clase base para gestión de vehículos";
  }
}

console.log(AutoLarrota.informacionGeneralLarrota());

const carroLarrota = new AutoLarrota("Ford", "Focus");


//¿Cuándo usar métodos estáticos?
//Funciones de utilidad relacionadas con la clase
//Métodos que no necesitan propiedades de instancia
//Operaciones a nivel de clase, no de objeto