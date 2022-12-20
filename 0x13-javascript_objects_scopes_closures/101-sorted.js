#!/usr/bin/node

const dict = require('./101-data').dict;
const values = Object.values(dict);
const entries = Object.entries(dict);
const uniqValues = [...new Set(values)];
const newObj = {};
for (const i in uniqValues) {
  const li = [];
  for (const j in entries) {
    if (entries[j][1] === uniqValues[i]) {
      li.push(entries[j][0]);
	}
  }
  newObj[uniqValues[i]] = li;
}
console.log(newObj);
