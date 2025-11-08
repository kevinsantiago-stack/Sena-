(function(){
function fib(n){ if(n<2) return n; return fib(n-1)+fib(n-2); }
let n = parseInt(prompt("n para fibonacci recursivo:"));
if (isNaN(n)||n<0) { alert("Inválido"); } else { alert("fib(" + n + ") = " + fib(n)); }
})();