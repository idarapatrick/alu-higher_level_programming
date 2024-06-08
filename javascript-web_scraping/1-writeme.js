#!/usr/bin/node
const fs = require('fs');
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

fs.writeFileSync(filePath, stringToWrite, 'utf-8', function (error) {
  if (error) {
    console.error(error);
  }
});
