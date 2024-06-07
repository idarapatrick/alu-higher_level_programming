#!/usr/bin/node
let narg = 0; // number of arg

exports.logMe = function (item) {
  console.log(narg + ': ' + item);
  narg++;
};
