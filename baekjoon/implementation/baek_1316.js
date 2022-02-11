const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const num = Number(input.shift());
let ans = 0;

for (let i = 0; i < num; i++) {
    let word = input.shift();
    let arr = new Array();
    let tmp = '';
    let check = true;
    for (let i of word) {
        if (arr.indexOf(i) >= 0) {

            if (tmp === i) continue;
            else {
                check = false;
                break
            };
        }
        arr.push(i);
        tmp = i;
    }
    if (check) ans++;
}

console.log(ans);
