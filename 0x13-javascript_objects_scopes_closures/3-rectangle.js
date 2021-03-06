#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.height = h;
      this.width = w;
    }
  }

  // Print rectangle using the character 'X'
  print () {
    for (let i = this.height; i--;) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
