(function(){
let a = parseInt(prompt("Ingrese el primer entero:"));
let b = parseInt(prompt("Ingrese el segundo entero:"));
if (isNaN(a) || isNaN(b)) { alert("Entrada inválida"); }
else {
  function gcd(x,y){ x=Math.abs(x); y=Math.abs(y); while(y){ let t=x%y; x=y; y=t; } return x; }
  let g = gcd(a,b);
  let l = Math.abs(a*b)/g;
  alert("MCD: " + g + "\nMCM: " + l);
}
})();