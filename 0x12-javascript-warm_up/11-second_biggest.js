#!/usr/bin/node
const cmdarguments = process.argv;
if (!cmdarguments[2] || (cmdarguments[2] && !cmdarguments[3])) {
  console.log(0);
} else {
  let temp, second;
  let largest = Number(cmdarguments[2]);
  let i = 3;
  while (cmdarguments[i]) {
    temp = Number(cmdarguments[i]);
    // if current number is the largest, shift it in
    if (temp > largest) {
      second = largest;
      largest = temp;
    // if its second largest, store it in second
    } else if (!second || (temp > second)) {
      second = temp;
    }
    i++;
  }
  console.log(second);
}
