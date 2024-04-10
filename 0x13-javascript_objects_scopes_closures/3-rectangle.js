#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (h > 0 && w > 0) {
      this.width = w;
      this.height = h;
    }
  }

  // prints the rectangle
  print () {
    let row = '';
    for (let j = 0; j < this.width; j++) {
      row += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(row);
    }
  }
}
module.exports = Rectangle;
