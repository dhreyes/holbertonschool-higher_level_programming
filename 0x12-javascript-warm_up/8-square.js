#!/usr/bin/node
let square = '';
const myArgs = parseInt(process.argv[2]);
if (isNaN(myArgs)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < myArgs; i++) {
    square = square.concat('X');
  }
  for (let j = 0; j < myArgs; j++) {
    console.log(square);
  }
}
