(function(){
let txt = prompt("Texto:");
let shift = parseInt(prompt("Desplazamiento:"));
if (!txt || isNaN(shift)) { alert("Inválido"); }
else {
  let out = "";
  for(let ch of txt){
    let c=ch.charCodeAt(0);
    if(c>=65 && c<=90) out += String.fromCharCode(((c-65+shift)%26+26)%26+65);
    else if(c>=97 && c<=122) out += String.fromCharCode(((c-97+shift)%26+26)%26+97);
    else out += ch;
  }
  alert(out);
}
})();