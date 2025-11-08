(function(){
let pwd = prompt("Ingrese una contraseña:");
if (pwd===null) { alert("Operación cancelada"); }
else { alert(pwd.length >= 8 ? "Contraseña válida" : "Contraseña demasiado corta"); }
})();