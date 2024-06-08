#!/usr/bin/node

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor(size) {
    // Call the Rectangle constructor with size as both width and height
    super(size, size);
  }
};
