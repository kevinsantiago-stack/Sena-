(function(){
let t = prompt("Ingrese texto:");
if (!t) { alert("0"); }
else { let c = t.trim().split(/\s+/).filter(x=>x!=="").length; alert("Palabras: " + c); }
})();