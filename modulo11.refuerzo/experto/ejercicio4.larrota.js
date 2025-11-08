self.onmessage = function(e) {
  const { tipo, data } = e.data;
  switch (tipo) {
    case "procesarArray":
      const resultado = data.map(x => x * 2).filter(x => x > 10);
      self.postMessage(resultado);
      break;
    case "fibonacci":
      function fibonacci(n) {
        let [a, b] = [0, 1];
        const seq = [];
        for (let i = 0; i < n; i++) {
          seq.push(a);
          [a, b] = [b, a + b];
        }
        return seq;
      }
      self.postMessage(fibonacci(data));
      break;
  }
};

const worker = new Worker("worker.js");

worker.postMessage({ tipo: "procesarArray", data: [1,2,3,4,5,6,7,8] });

worker.onmessage = function(e) {
  console.log("Resultado:", e.data);
};
