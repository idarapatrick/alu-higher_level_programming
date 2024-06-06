#!/usr/bin/node
const [argOne, argTwo] = process.argv.slice(2);
if (!argOne || !argTwo) {
  console.log(`${argOne} is undefined`);
} else {
  console.log(`${argOne} is ${argTwo}`);
}
