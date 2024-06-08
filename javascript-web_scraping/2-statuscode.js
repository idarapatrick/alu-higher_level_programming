#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, res) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(`code: ${res.statusCode}`);
});
