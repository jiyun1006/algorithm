// 회의실 배정

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let [num, ...input] = fs.readFileSync("./ex.txt").toString().trim().split('\n');


const arr = input.map(a => a.split(" ").map(Number)).sort((a, b) => {
    if (a[1] === b[1]) return a[0] - b[0];
    else return a[1] - b[1];

})


let cnt = 0;
let end = 0;

for (let i of arr) {
    if (i[0] >= end) {
        end = i[1];
        cnt++;
    }
}

console.log(cnt);