const miIterable = {
  desde: 1,
  hasta: 5,
  [Symbol.iterator]() {
    let actual = this.desde;
    const ultimo = this.hasta;
    return {
      next() {
        if (actual <= ultimo) {
          return { value: actual++, done: false };
        } else {
          return { done: true };
        }
      }
    };
  }
};

for (let num of miIterable) {
  console.log(num); 
}