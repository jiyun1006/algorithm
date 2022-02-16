const fs = require("fs");
const { isBuffer } = require("util");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().split('\n').map(Number);

let sum = input.reduce((a, b) => a + b);
console.log(sum);
let answer = [];

for (let i = 0; i < 9; i++) {
    if (answer.length > 0) break;
    for (let j = i + 1; j < 9; j++) {
        if (sum - input[i] - input[j] === 100) {
            answer = input.filter((_, idx) => idx !== i && idx !== j).
                sort((a, b) => a - b); // _는 값 a는 index
            answer = answer.join("\n");
            console.log(answer);
            break;
        }
    }
}