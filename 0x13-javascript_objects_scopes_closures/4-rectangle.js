#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // Print rectangle using char 'X'
  print () {
    for (let i = this.height; i--;) {
      console.log('X'.repeat(this.width));
    }
  }

  // Exchange width and height of Rectangle
  rotate () {
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  // Double height and width of Rectangle
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
