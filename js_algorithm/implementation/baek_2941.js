const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim();

const arr = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="];
let ans = 0;
for (let i of arr) {
    while (input.indexOf(i) >= 0) {

        input = input.replace(i, ' ');

        ans++;
    }
}
input = input.replaceAll(' ', '');
ans += input.length;
console.log(ans);