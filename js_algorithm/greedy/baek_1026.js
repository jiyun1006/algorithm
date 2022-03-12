// 보물

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const num = Number(input.shift());

let A = input[0].split(" ").map((el) => +el);
let B = input[1].split(" ").map((el) => +el);
A = A.sort((a, b) => a - b);
B = B.sort((a, b) => b - a);

let ans = 0;
for (let i = 0; i < num; i++) {
    ans += A[i] * B[i];
}

console.log(ans);