#!/usr/bin/node
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let s = '';
        for (let j = 0; j < this.width; j++) {
          s += c;
        }
        console.log(s);
      }
    }
  }
};
