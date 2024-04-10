#!/usr/bin/node
exports.converter = function (base) {
  function baseConverter (number) {
    return (number.toString(base));
  };
  return baseConverter;
};
