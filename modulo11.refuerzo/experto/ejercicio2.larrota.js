class Observable {
  constructor() {
    this.observadores = [];
  }
  suscribir(obs) {
    this.observadores.push(obs);
  }
  desuscribir(obs) {
    this.observadores = this.observadores.filter(o => o !== obs);
  }
  notificar(datos) {
    this.observadores.forEach(o => o(datos));
  }
}


const notificaciones = new Observable();

const obs1 = msg => console.log("Obs1:", msg);
const obs2 = msg => console.log("Obs2:", msg);

notificaciones.suscribir(obs1);
notificaciones.suscribir(obs2);

notificaciones.notificar("¡Nuevo mensaje!");


notificaciones.desuscribir(obs2);
notificaciones.notificar("Segundo mensaje");
