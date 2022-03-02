const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const test = Number(input.shift());

for (let i = 0; i < test; i++) {
    const [N, M] = input.shift().split(" ").map((el) => +el);
    let arr = input.shift().split(" ").map((el) => +el);
    let tmpArr = [...arr];
    tmpArr = tmpArr.sort((a, b) => b - a);

    let idx = 0;
    let ans = 1;
    let bool = false;
    while (true) {
        let max = tmpArr.shift();
        while (true) {
            let tmp = arr.shift();
            if (tmp === max) {
                if (idx === M) {
                    bool = true;
                    break;
                }
                ans++;
                idx = (idx + 1) % N;
                arr.push(tmp);
                break;
            } else {
                idx = (idx + 1) % N;
            }
            arr.push(tmp);
        }
        if (bool) break;
    }
    console.log(ans);
}