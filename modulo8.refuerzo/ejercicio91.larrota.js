(function(){
let faces = parseInt(prompt("Caras del dado:")) || 6;
let rolls = parseInt(prompt("Número de lanzamientos:")) || 1;
let res = [];
for(let i=0;i<rolls;i++) res.push(Math.floor(Math.random()*faces)+1);
alert("Resultados: " + res.join(", "));
})();