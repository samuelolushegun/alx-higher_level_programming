#!/usr/bin/node
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  let big = 0;
  let big2 = 0;
  for (let i = 2; i < args.length; i++) {
    if (parseInt(args[i]) >= big) {
      big2 = big;
      big = parseInt(args[i]);
    } else if (parseInt(args[i]) > big2 && parseInt(args[i]) !== big) {
      big2 = parseInt(args[i]);
    }
  }
  console.log(big2);
}
