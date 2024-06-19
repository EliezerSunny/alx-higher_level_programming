#!/usr/bin/node
const args = process.argv;

const firstArg = args[2] !== undefined ? args[2] : "No argument";

console.log(firstArg);
