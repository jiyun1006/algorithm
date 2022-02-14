const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const num = Number(input.shift());
for (let i = 0; i < num; i++) {
    let tmp = Number(input.shift());
    let dpZero = [1, 0];
    let dpOne = [0, 1];
    if (tmp === 0) {
        console.log(dpZero[tmp] + " " + dpOne[tmp]);
        continue;
    }
    else if (tmp === 1) {
        console.log(dpZero[tmp] + " " + dpOne[tmp]);
        continue;
    }
    else {
        for (let j = 2; j <= tmp; j++) {
            dpZero[j] = dpZero[j - 1] + dpZero[j - 2];
            dpOne[j] = dpOne[j - 1] + dpOne[j - 2];
        }
        console.log(dpZero[tmp] + " " + dpOne[tmp]);
    }

}
//   0 1 2 3 4 5 6
// 0:1 0 1 1 2 3 5
// 1:0 1 1 2 3 5 8