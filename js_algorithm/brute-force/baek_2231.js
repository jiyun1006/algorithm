const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString();

let len = input.length;

input = Number(input);
const min = (input - 9 * len) < 0 ? 0 : (input - 9 * len);

for (i = min; i < input; i++) {
    tmp = 0;
    tmpLen = len;
    tmpNum = i;
    while (tmpLen > 0) {
        tmp += Math.floor(tmpNum / (10 ** (tmpLen - 1)));
        tmpNum %= (10 ** (tmpLen - 1));
        tmpLen--;
    }

    if (i + tmp === input) {
        console.log(i);
        return;
    }

}

console.log(0);

