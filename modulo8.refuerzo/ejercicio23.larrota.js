(function(){
let mes = parseInt(prompt("Ingrese número de mes (1-12):"));
let est="";
switch(mes){
case 12: case 1: case 2: est="Invierno"; break;
case 3: case 4: case 5: est="Primavera"; break;
case 6: case 7: case 8: est="Verano"; break;
case 9: case 10: case 11: est="Otoño"; break;
default: est="Mes inválido";
}
alert(est);
})();