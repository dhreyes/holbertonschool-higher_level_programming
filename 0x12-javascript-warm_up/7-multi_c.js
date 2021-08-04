#!/usr/bin/node

let myArgs = parseInt(process.argv[2]);
if (isNaN(myArgs)) {
  console.log('Missing number of occurences');
} else {
  while (myArgs > 0) {
    console.log('C is fun');
    myArgs--;
  }
}
