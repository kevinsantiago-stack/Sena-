(function(){
function suma(a,b){ return a+b; }
function resta(a,b){ return a-b; }
function mult(a,b){ return a*b; }
function div(a,b){ return b===0? "Error": a/b; }
let a=parseFloat(prompt("a:")), b=parseFloat(prompt("b:")), op=prompt("op (+ - * /):");
let r = op==='+'?suma(a,b):op==='-'?resta(a,b):op==='*'?mult(a,b):op==='/'?div(a,b):"op inválido";
alert(r);
})();