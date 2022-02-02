#!/usr/bin/node
// Write a script that writes a string to a file
// The script should take a string and a file name as arguments
// The script should write the string to the file

const fs = require('fs');
const fileName = process.argv[2];
const text = process.argv[3];

fs.writeFile(fileName, text, (err) => {
  if (err) {
    console.log(err);
  }
});
