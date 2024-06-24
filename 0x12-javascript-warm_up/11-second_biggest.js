#!/usr/bin/node
let nextmax = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.sort();
  nextmax = args[args.length - 2];
}
console.log(nextmax);
