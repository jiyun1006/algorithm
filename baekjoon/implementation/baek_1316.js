const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const num = Number(input.shift());


for (let i = 0; i < num; i++) {

}

