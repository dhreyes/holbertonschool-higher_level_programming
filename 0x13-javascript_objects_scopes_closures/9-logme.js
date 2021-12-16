#!/usr/bin/node

let count = 0;
exports.logMe = function (mcguffin) {
  console.log(count + ': ' + mcguffin);
  count++;
};
