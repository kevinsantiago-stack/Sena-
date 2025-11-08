(function(){
let raw = prompt("Datos separados por comas (nombres:valor):");
if (!raw) { alert("No hay datos"); }
else {
  let items = raw.split(",").map(x=>x.split(":"));
  let total = items.reduce((s,kv)=>s + (parseFloat(kv[1])||0),0);
  alert("Total: " + total + "\nElementos: " + items.length);
}
})();