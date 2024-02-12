#!/usr/bin/node
function fact (x) {
  if (x === 0 || isNaN(x)) {
    return (1);
  } else {
    return (x * fact(x - 1));
  }
}
console.log(fact(parseInt(process.argv[2])));
