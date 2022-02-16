const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = Number(fs.readFileSync("./ex.txt").toString());
const div = Math.floor(input / 5);
const ansList = new Array();


const solution = (big, small, div, ansList) => {
    for (i = div; i > 0; i--) {
        const tmp = input - (big * i);
        if (tmp % small === 0) {
            ansList.push((i + tmp / small));
        }
    }
    if (ansList.length !== 0) {
        return Math.min.apply(null, ansList);
    } else {

        if (input % small === 0) {
            return input / small;
        }
        else {
            return -1;
        }
    }
}

const ans = solution(5, 3, div, ansList);
console.log(ans);