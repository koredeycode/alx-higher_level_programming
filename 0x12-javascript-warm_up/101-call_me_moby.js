#!/usr/bin/node
exports.callMeMoby = function (x, func) {
  let i = 0;
  while (i < x) {
    func();
    i -= -1;
  }
};
