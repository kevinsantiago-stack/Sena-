(function(){
let tipo = prompt("Figura (círculo,triángulo,rectángulo,cuadrado):").toLowerCase();
if (tipo==="círculo"||tipo==="circulo"){
  let r = parseFloat(prompt("Radio:"));
  if (isNaN(r)) { alert("Inválido"); } else { alert("Área: " + (Math.PI*r*r).toFixed(2) + " Perímetro: " + (2*Math.PI*r).toFixed(2)); }
} else if (tipo==="triángulo"||tipo==="triangulo"){
  let b=parseFloat(prompt("Base:")), h=parseFloat(prompt("Altura:"));
  if (isNaN(b)||isNaN(h)) { alert("Inválido"); } else { alert("Área: " + (b*h/2).toFixed(2)); }
} else if (tipo==="rectángulo"||tipo==="rectangulo"){
  let a=parseFloat(prompt("Largo:")), c=parseFloat(prompt("Ancho:"));
  if (isNaN(a)||isNaN(c)) { alert("Inválido"); } else { alert("Área: " + (a*c).toFixed(2) + " Perímetro: " + (2*(a+c)).toFixed(2)); }
} else if (tipo==="cuadrado"){
  let l=parseFloat(prompt("Lado:"));
  if (isNaN(l)) { alert("Inválido"); } else { alert("Área: " + (l*l).toFixed(2) + " Perímetro: " + (4*l).toFixed(2)); }
} else { alert("Figura inválida"); }
})();