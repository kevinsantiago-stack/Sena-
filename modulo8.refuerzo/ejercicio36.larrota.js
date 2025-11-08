(function(){
let n = parseInt(prompt("Ingrese la cantidad de términos (n):"));
if (isNaN(n) || n<1) { alert("Entrada inválida"); }
else {
  let a=0,b=1,msg="";
  for(let i=1;i<=n;i++){ msg += a + ((i<n)?" ":""); let c=a+b; a=b; b=c; }
  alert(msg);
}
})();