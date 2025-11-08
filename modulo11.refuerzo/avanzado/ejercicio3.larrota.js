function* generadorContador() {
  let i = 0;
  while (true) {
    yield i++;
  }
}

const contador = generadorContador();
console.log(contador.next().value); // 0
console.log(contador.next().value); // 1
console.log(contador.next().value); // 2