#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      this.width = 0
      this.height = 0
    }
  }
  
  print() {
    console.log(`Rectangle(width: ${this.width}, height: ${this.height})`);
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }
  
  
  rotate () {
    const currentState = this.width;
    this.width = this.height;
    this.height = currentState;
  }
  
  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
