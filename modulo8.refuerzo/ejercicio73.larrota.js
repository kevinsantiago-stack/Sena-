(function(){
let raw = prompt("Elementos separados por comas:");
let k = parseInt(prompt("Rotar k posiciones a la derecha:"));
if (!raw || isNaN(k)) { alert("Entrada inválida"); }
else {
  let arr = raw.split(",").map(x=>x.trim());
  k = ((k%arr.length)+arr.length)%arr.length;
  let res = arr.slice(-k).concat(arr.slice(0,-k));
  alert("Resultado: " + res.join(", "));
}
})();