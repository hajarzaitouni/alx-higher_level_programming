#!/usr/bin/node
const size = process.argv[2];
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let r = '';
    for (let j = 0; j < size; j++) {
      r += 'X';
    }
    console.log(r);
  }
}
