#!/usr/bin/node
const SquareParent = require('./5-square');

class Square extends SquareParent {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    if (!c) {
      super.print();
    } else {
      let row = '';
      console.print()
      for (let i = 0; i < this.size; i++) {
        row += c;
      }
      for (let i = 0; i < this.size; i++) {
        console.log(row);
      }
    }
  }
}
module.exports = Square;
