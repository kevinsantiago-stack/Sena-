(function(){
let tipo = prompt("Convertir: m->ft, kg->lb, l->gal (escribe m,kg,l):");
if (tipo==="m"){ let m=parseFloat(prompt("Metros:")); if(isNaN(m)){alert("Inválido")}else{alert(m + " m = " + (m*3.28084).toFixed(4) + " ft")}}
else if (tipo==="kg"){ let k=parseFloat(prompt("Kg:")); if(isNaN(k)){alert("Inválido")}else{alert(k + " kg = " + (k*2.20462).toFixed(4) + " lb")}}
else if (tipo==="l"){ let L=parseFloat(prompt("Litros:")); if(isNaN(L)){alert("Inválido")}else{alert(L + " l = " + (L*0.264172).toFixed(4) + " gal")}}
else { alert("Opción inválida"); }
})();