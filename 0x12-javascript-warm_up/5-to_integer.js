#!/usr/bin/env node

const myArgs = parseInt(process.argv[2]);
if (isNaN(myArgs)) {
console.log('Not a number');
} else {
	console.log('My number: ' + myArgs);
}
