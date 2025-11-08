(function(){
let user = prompt("Usuario:");
let pass = prompt("Contraseña:");
let ok = (user==="admin" && pass==="1234") ? "Autenticado" : "Acceso denegado";
alert(ok);
})();