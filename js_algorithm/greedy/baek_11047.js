// 동전 0

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

let [N, K] = input.shift().split(" ").map(Number);
let arr = new Array();

for (let i = 0; i < N; i++) {
    arr.push(Number(input.shift()));
}

arr = arr.sort((a, b) => b - a);

let ans = 0;
for (let num of arr) {
    if (num <= K) {
        if (K % num === 0) {
            ans += K / num;
            break;
        }
        ans += Math.floor(K / num);
        K = K % num;
    }
}
console.log(ans);