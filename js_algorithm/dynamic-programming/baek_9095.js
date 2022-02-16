const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const num = Number(input.shift());
let arr = [1, 2, 4];


for (let i = 0; i < num; i++) {
    let tmp = Number(input.shift());
    for (let j = 3; j < tmp; j++) {
        arr[j] = arr[j - 3] + arr[j - 2] + arr[j - 1];
    }
    console.log(arr[tmp - 1]);
}

