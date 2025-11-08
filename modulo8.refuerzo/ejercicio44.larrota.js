(function(){
let limit = parseInt(prompt("Listar primos hasta:"));
if (isNaN(limit) || limit<2) { alert("Inválido"); }
else {
  let primes=[];
  for(let n=2;n<=limit;n++){
    let p=true;
    for(let i=2;i<=Math.sqrt(n);i++) if(n%i===0){ p=false; break; }
    if(p) primes.push(n);
  }
  alert("Primos: " + primes.join(", "));
}
})();