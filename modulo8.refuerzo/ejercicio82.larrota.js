(function(){
let len = parseInt(prompt("Longitud de la contraseña:"));
if (isNaN(len) || len<1) { alert("Inválido"); }
else {
  let chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*";
  let s="";
  for(let i=0;i<len;i++) s += chars.charAt(Math.floor(Math.random()*chars.length));
  alert(s);
}
})();