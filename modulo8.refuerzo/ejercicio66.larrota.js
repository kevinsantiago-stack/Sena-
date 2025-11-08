(function(){
let raw = prompt("Ingrese números separados por comas:");
if (!raw) { alert("Entrada vacía"); }
else {
  let arr = raw.split(",").map(x=>parseFloat(x.trim())).filter(x=>!isNaN(x));
  let s = arr.reduce((a,b)=>a+b,0);
  alert("Suma: " + s);
}
})();