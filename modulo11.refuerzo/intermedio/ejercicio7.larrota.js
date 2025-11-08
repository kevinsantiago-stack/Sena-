function simularAPI(datos, tiempo) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (datos) {
        resolve(`Datos procesados: ${datos}`);
      } else {
        reject('Error: No hay datos');
      }
    }, tiempo);
  });
}

simularAPI("Usuario 1", 1000)
  .then(resultado => console.log(resultado))
  .catch(error => console.error(error));