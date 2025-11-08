async function procesarDatos() {
  try {
    console.log("Iniciando procesamiento...");

    const resultado1 = await simularAPI("Usuario 1", 1000);
    console.log(resultado1);

    const resultado2 = await simularAPI("Usuario 2", 500);
    console.log(resultado2);

    console.log("Procesamiento completado");
  } catch (error) {
    console.error("Error:", error);
  }
}

procesarDatos();