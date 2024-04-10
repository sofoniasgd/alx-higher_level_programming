#!/usr/bin/node
exports.converter = function (base) {
  const baseConverter = function (number) {
    return (number.toString(base));
  };
  return baseConverter;
};
