try {
  throw new Error("Algo salió mal, larrota");
} catch (e) {
  console.log("Error capturado:", e.message);
}
