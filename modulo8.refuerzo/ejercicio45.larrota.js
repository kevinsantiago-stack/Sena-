(function(){
let rows = parseInt(prompt("Filas:"));
let cols = parseInt(prompt("Columnas:"));
if (isNaN(rows)||isNaN(cols)||rows<1||cols<1){ alert("Inválido"); }
else {
  let s=0;
  for(let r=0;r<rows;r++){
    for(let c=0;c<cols;c++){
      let v = parseFloat(prompt("Elemento ["+r+","+c+"]:"));
      s += isNaN(v)?0:v;
    }
  }
  alert("Suma total: " + s);
}
})();