#!/usr/bin/node
exports.converter = function (base) {
  return function covertBase (number) {
    return number.toString(base);
  };
};
