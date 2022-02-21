//ATM

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const num = Number(input.shift());
let time = input.shift().split(" ").map(Number);
time = time.sort((a, b) => a - b);

let tmp = 0;
let ans = 0;

for (let i of time) {
    tmp += i;
    ans += tmp;
}
console.log(ans);