const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().split('\n');

let N = Number(input.shift());
const F = input.shift();

N = N - N % 100;

while (N % F !== 0) {
    N++;
}

N = N.toString();

console.log(N.slice(-2));