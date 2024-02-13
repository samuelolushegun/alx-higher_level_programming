#!/usr/bin/node

exports.esrever = function (list) {
  const reverslist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reverslist.push(list[i]);
  }
  return (reverslist);
};
