#!/usr/bin/node
const [arg] = process.argv.slice(2);
if (!arg) {
  console.log('No argument');
} else {
  console.log(arg);
}
