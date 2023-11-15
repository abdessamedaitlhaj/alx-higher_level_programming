#!/usr/bin/node
/* Function that returns the reversed version of a list */

exports.esrever = function (list) {
  let listItem;
  let i = 0;
  while (i < list.length / 2) {
    listItem = list[i];
    list[i] = list[list.length - i - 1];
    list[list.length - i - 1] = listItem;
    i++;
  }
  return (list);
};
