#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.slice(2);

const v1 = fs.readFileSync(argv[0]).toString();
const v2 = fs.readFileSync(argv[1]).toString();

fs.writeFileSync(argv[2], v1 + v2);
