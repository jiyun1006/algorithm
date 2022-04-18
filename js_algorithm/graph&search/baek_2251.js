// 물통

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split(' ').map((el) => +el);
const A = input[0];
const B = input[1];
const C = input[2];

const ans = new Array();

ans.push(C - B);
ans.push(C - A);
ans.push(A, B, C);

ans.sort((a, b) => a - b);
console.log(ans.join(' '));