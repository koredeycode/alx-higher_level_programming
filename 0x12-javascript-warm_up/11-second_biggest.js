#!/usr/bin/node
const arr = process.argv.slice(2);
arr.sort(function (a, b) { return (b - a); });
if (arr[1]) {
  console.log(arr[1]);
} else {
  console.log(0);
}
