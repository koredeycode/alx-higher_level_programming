#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else {
  let count = parseInt(process.argv[2]);
  while (count > 0) {
    console.log('C is fun');
    count -= 1;
  }
}
