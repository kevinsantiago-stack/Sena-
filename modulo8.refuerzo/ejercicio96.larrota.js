(function(){
let d = prompt("Fecha (yyyy-mm-dd):");
if (!d) { alert("Vacío"); }
else {
  let p = d.split("-");
  if (p.length!==3) { alert("Formato inválido"); }
  else { alert(p[2] + "/" + p[1] + "/" + p[0]); }
}
})();