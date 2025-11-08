(function(){
let a = (prompt("Array A (comas):")||"").split(",").map(x=>x.trim()).filter(x=>x!=="");
let b = (prompt("Array B (comas):")||"").split(",").map(x=>x.trim()).filter(x=>x!=="");
let union = Array.from(new Set(a.concat(b)));
let intersection = a.filter(x=>b.indexOf(x)!==-1);
alert("Unión: " + union.join(", ") + "\nIntersección: " + intersection.join(", "));
})();