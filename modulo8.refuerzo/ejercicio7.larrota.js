(function(){
let peso = parseFloat(prompt("Peso en kg:"));
let altura = parseFloat(prompt("Altura en metros:"));
if (isNaN(peso) || isNaN(altura) || altura<=0) { alert("Entrada inválida"); }
else { let imc = peso/(altura*altura); let cat = (imc<18.5)?"Bajo peso":(imc<25)?"Normal":(imc<30)?"Sobrepeso":"Obesidad"; alert(imc.toFixed(2) + " - " + cat); }
})();