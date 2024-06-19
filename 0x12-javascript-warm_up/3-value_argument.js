#!/usr/bin/node
const args = process.argv.slice(2);

const firstArg = args[0] !== undefined ? args[0] : "No argument";

console.log(firstArg);
