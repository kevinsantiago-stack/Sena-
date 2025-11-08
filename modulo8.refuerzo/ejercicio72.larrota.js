(function(){
let raw = prompt("Elementos separados por comas:");
if (!raw) { alert("Entrada vacía"); }
else {
  let arr = raw.split(",").map(x=>x.trim());
  let uniques = arr.filter((v,i,a)=>a.indexOf(v)===i);
  alert("Únicos: " + uniques.join(", "));
}
})();