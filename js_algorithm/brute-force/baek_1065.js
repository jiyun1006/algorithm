// 한수

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim();


if (+input < 100) console.log(input);
else {
    let ans = 99;
    for (let i = 100; i <= +input; i++) {
        let num = i.toString().split("").map((el) => +el);
        for (let j = 1; j < num.length - 1; j++) {
            if (num[j] - num[j - 1] !== num[j + 1] - num[j]) {
                break;
            }
            if (j === num.length - 2) ans++;
        }
    }
    console.log(ans);
}