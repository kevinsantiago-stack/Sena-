(function(){
let d = parseInt(prompt("Ingrese número del día (1-7):"));
let name = "";
switch(d){
case 1: name="Lunes"; break;
case 2: name="Martes"; break;
case 3: name="Miércoles"; break;
case 4: name="Jueves"; break;
case 5: name="Viernes"; break;
case 6: name="Sábado"; break;
case 7: name="Domingo"; break;
default: name="Valor inválido";
}
alert(name);
})();