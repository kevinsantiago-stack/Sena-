(function(){
let num1 = parseFloat(prompt("Ingrese primer número:"));
let op = prompt("Operación (+ - * /):");
let num2 = parseFloat(prompt("Ingrese segundo número:"));
let res;
switch(op){
case '+': res = num1 + num2; break;
case '-': res = num1 - num2; break;
case '*': res = num1 * num2; break;
case '/': res = (num2!==0)? num1/num2 : "Error"; break;
default: res = "Operación inválida";
}
alert(res);
})();