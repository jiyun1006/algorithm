// 요세푸스 문제 0

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const [N, K] = fs.readFileSync("./ex.txt").toString().trim().split(" ").map((el) => +el);

const arr = new Array(N).fill().map((_, idx) => idx + 1);

let idx = 0;
let ans = new Array();
while (arr.length) {
    idx += K - 1;
    if (idx >= arr.length) idx %= arr.length;
    let tmp = arr.splice(idx, 1);
    ans.push(...tmp);
}
console.log("<" + ans.join(", ") + ">");