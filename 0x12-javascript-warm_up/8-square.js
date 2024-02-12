#!/usr/bin/node
const size = process.argv[2];
if (isNaN(parseInt(size))) {
  console.log('Missing size');
} else {
  let line = '';
  for (let i = 0; i < size; i++) {
    line += 'X';
  }
  for (let x = 0; x < size; x++) {
    console.log(line);
  }
}
