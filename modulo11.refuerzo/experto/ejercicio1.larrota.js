const MiModulo = (function() {
  
  let contadorPrivado = 0;
  const datosPrivados = [];

  function metodoPrivado() {
    console.log("Este método es privado");
  }

  return {
    incrementar: function() {
      contadorPrivado++;
      metodoPrivado();
      return contadorPrivado;
    },
    agregarDato: function(dato) {
      datosPrivados.push(dato);
      return datosPrivados.length;
    },
    obtenerContador: function() {
      return contadorPrivado;
    }
  };
})();

console.log(MiModulo.incrementar()); 
console.log(MiModulo.agregarDato("Hola")); 
console.log(MiModulo.obtenerContador()); 