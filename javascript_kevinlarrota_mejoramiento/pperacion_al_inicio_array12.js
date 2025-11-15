let Larrota = ["Cliente A", "Cliente B", "Cliente C"];
console.log("Cola inicial:", Larrota);

let cuervo = Larrota.shift();
console.log("Cliente atendido:", cuervo);
console.log("Cola después de shift:", Larrota);

Larrota.unshift("Cliente Prioritario");
console.log("Cola final:", Larrota);

//shift() - Remover del inicioElimina y retorna el primer elemento. Todos losdemás elementos se desplazan una posición haciaadelante.
//unshift() - Agregar al inicioAñade elementos al inicio. Todos los elementos existentes se desplazan una posición hacia atrás.