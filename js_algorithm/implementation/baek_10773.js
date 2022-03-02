const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const num = Number(input.shift());

let arr = new Array();
for (let i = 0; i < num; i++) {
    if (input[i] === "0") {
        arr.pop();
        continue;
    }
    arr.push(input[i]);
}


if (arr.length === 0) console.log(0);
else console.log(arr.reduce((a, b) => {
    return +a + +b;
}))

