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

  // exchanges width and height
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // multiplies the width and height by 2
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
