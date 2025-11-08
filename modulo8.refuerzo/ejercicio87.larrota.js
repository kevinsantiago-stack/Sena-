(function(){
let num = prompt("Número tarjeta:").replace(/\s+/g,'');
if (!/^[0-9]+$/.test(num)) { alert("Inválido"); }
else {
  let sum=0, alt=false;
  for(let i=num.length-1;i>=0;i--){
    let d = parseInt(num[i]);
    if(alt){ d*=2; if(d>9) d-=9; }
    sum += d; alt = !alt;
  }
  alert((sum%10===0) ? "Válido" : "Inválido");
}
})();