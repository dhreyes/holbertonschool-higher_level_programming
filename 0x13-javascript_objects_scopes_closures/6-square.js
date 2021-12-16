#!/usr/bin/node

// Inherit from Square Rectangle class in module 5-square.js
class Square extends require('./5-square') {
  constructor (size) {
    super(size, size);
  }

  // Print Square using given char or if no char is specified
  // it defauls to parent class
  charPrint (c = 'X') {
    for (let i = this.height; i--;) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
