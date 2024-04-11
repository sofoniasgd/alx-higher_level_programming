#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  constructor (size) {
    super(size);
    this.size = this.width;
  }

  // USE "this.width || this.length" INSTEAD OF "this.size"
  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      let row = '';
      for (let i = 0; i < this.width; i++) {
        row += c;
      }
      for (let i = 0; i < this.width; i++) {
        console.log(row);
      }
    }
  }
}
module.exports = Square;
