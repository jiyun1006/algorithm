const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = Number(fs.readFileSync("./ex.txt").toString().trim());

let A = [1, 0];
let B = [0, 1];

for (let i = 1; i < input; i++) {
    A[i + 1] = A[i] + A[i - 1];
    B[i + 1] = B[i] + B[i - 1];
}
console.log(A[A.length - 1], B[B.length - 1]);

// A B BA BAB BABBA BABBABAB BABBABABBABBA
// 1 0 1  1  2  3  5
// 0 1 1  2  3  5  8