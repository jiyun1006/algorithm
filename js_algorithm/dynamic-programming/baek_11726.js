const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = Number(fs.readFileSync('./ex.txt').toString().trim());

let ans = [0, 1];

for (let i = 2; i < input + 2; i++) {
    ans[i] = (ans[i - 1] + ans[i - 2]) % 10007;
}
console.log(ans.pop());