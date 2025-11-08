const validador = {
  set(obj, prop, valor) {
    if (prop === "edad") {
      if (!Number.isInteger(valor) || valor < 0 || valor > 150) {
        throw new Error("Edad debe estar entre 0 y 150");
      }
    }
    if (prop === "email") {
      const regex = /^\S+@\S+\.\S+$/;
      if (!regex.test(valor)) {
        throw new Error("Email no válido");
      }
    }
    obj[prop] = valor;
    return true;
  }
};

const persona = new Proxy({}, validador);
persona.nombre = "Ana";                   // OK
persona.edad = 25;                        // OK
persona.email = "ana@example.com";        // OK
// persona.edad = 200; // Error!