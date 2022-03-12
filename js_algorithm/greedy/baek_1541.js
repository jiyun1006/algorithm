// 잃어버린 괄호

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const arr = input.shift().split("-");

let ans = 0;
arr.map((el, idx) => {
    if (idx === 0) {
        ans = el.split("+").map((i) => +i).reduce((a, b) => a + b);
    }
    else {
        ans -= el.split("+").map((i) => +i).reduce((a, b) => a + b);
    }
})
console.log(ans);