#!/usr/bin/node
exports.nb0ccurences = function (list, searchElement) {
  let count = 0;
  for (let i = 0; list[i]; i++) {
    if (list[i] === searchElement) {
      count++;
    }
  }
  return count;
};
