#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0 && Number.isInteger(w) && Number.isInteger(h)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let wid = '';
    for (let i = 0; i < this.width; i++) {
      wid += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(wid);
    }
  }
}

module.exports = Rectangle;
