(function(){
let txt = prompt("Texto:");
let shift = parseInt(prompt("Desplazamiento:"));
if (!txt || isNaN(shift)) { alert("Inválido"); }
else {
  let out = "";
  for(let ch of txt){
    let c=ch.charCodeAt(0);
    if(c>=65 && c<=90) out += String.fromCharCode(((c-65+shift)%26+26)%26+65);
    else if(c>=97 && c<=122) out += String.fromCharCode(((c-97+shift)%26+26)%26+97);
    else out += ch;
  }
  alert(out);
}
})();

//ejercicio 101 larrota

(function(){
let a = parseFloat(prompt("a:")), b = parseFloat(prompt("b:"));
alert((a>b)?a:b);
})();


//ejercicio 102 larrota

(function(){
let n = parseInt(prompt("n:"));
alert((n%2===0)?"par":"impar");
})();

//ejercicio 103 larrota

(function(){
let n = parseFloat(prompt("n:"));
alert(n>0?"positivo":n<0?"negativo":"cero");
})();

//ejercicio 104 larrota

(function(){
let y = parseInt(prompt("Año:"));
alert(((y%4===0 && y%100!==0) || (y%400===0))?"sí":"no");
})();

//ejercicio 105 larrota

(function(){
let edad = parseInt(prompt("Edad:"));
alert(edad<18?"menor":(edad<65?"adulto":"senior"));
})();

//ejercicio 106 larrota


(function(){
let a=parseFloat(prompt("a:")), b=parseFloat(prompt("b:")), c=parseFloat(prompt("c:"));
alert((a===b && b===c)?"equilátero":(a===b || b===c || a===c)?"isósceles":"escaleno");
})();

//ejercicio 107 larrota

(function(){
let t = parseFloat(prompt("Temperatura (°C):"));
alert(t<=0?"sólido":(t<100?"líquido":"gaseoso"));
})();


//ejercicio 108 larrota

(function(){
let edad = parseInt(prompt("Edad:"));
let precio = parseFloat(prompt("Precio:"));
let d = (edad<12)?0.5:(edad>=65)?0.4:1;
alert("Precio final: " + (precio * d).toFixed(2));
})();

//ejercicio 109 larrota

(function(){
let d = parseInt(prompt("Día (1-7):"));
alert((d>=1 && d<=5)?"Laboral":"Fin de semana");
})();


//ejercicio 110 larrota

(function(){
let s = parseFloat(prompt("Puntuación (0-100):"));
alert(s>=90?"A":s>=80?"B":s>=70?"C":s>=60?"D":"F");
})();

