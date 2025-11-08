const logger = {
  get(obj, prop) {
    console.log(`Acceso: ${prop}`);
    return obj[prop];
  },
  set(obj, prop, valor) {
    console.log(`Cambio: ${prop} = ${valor}`);
    obj[prop] = valor;
    return true;
  }
};

const usuario = new Proxy({ nombre: "Juan" }, logger);
console.log(usuario.nombre);   
usuario.edad = 30;           