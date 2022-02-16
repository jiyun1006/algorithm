const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = Number(fs.readFileSync("./ex.txt").toString().trim());

const DP = [0, 1];

for (let i = 1; i < input; i++) {
    DP[i + 1] = BigInt(DP[i]) + BigInt(DP[i - 1]);
}

console.log(Number(DP[input]));