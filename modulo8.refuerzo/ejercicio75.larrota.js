(function(){
let rows=parseInt(prompt("Filas:"));
let cols=parseInt(prompt("Columnas:"));
if (isNaN(rows)||isNaN(cols)) { alert("Inválido"); }
else {
  let m = [];
  for(let r=0;r<rows;r++){
    m[r]=[];
    for(let c=0;c<cols;c++){
      m[r][c]=prompt("Elemento ["+r+","+c+"]:")||"";
    }
  }
  let t = [];
  for(let c=0;c<cols;c++){ t[c]=[]; for(let r=0;r<rows;r++) t[c][r]=m[r][c]; }
  alert("Transpuesta creada (ver consola)"); console.log(t);
}
})();