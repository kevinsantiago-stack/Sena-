let larrota = new Promise(resolve => {
  setTimeout(() => resolve("Promesa resuelta"), 1000);
});

larrota.then(console.log);
