const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const num = Number(input.shift());
const arr = new Array();

input.map((tmp) => {
    arr.push(tmp.split(" ").map(Number));
})

const check = (arr1, arr2, rank) => {
    if (arr1[0] < arr2[0]) {
        if (arr1[1] < arr2[1]) return rank + 1;
        else return rank;
    }
    else return rank;
}


const ans = new Array();

for (let i = 0; i < num; i++) {
    let rank = 1;
    for (let j = 0; j < num; j++) {
        if (i === j) continue;
        rank = check(arr[i], arr[j], rank);
    }
    ans.push(rank);
}

console.log(ans.join(' '));