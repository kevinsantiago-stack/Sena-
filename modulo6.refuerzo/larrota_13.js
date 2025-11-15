fetch("https://jsonplaceholder.typicode.com/todos/1")
  .then(r => r.json())
  .then(larrota => console.log(larrota));
