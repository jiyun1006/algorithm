const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = Number(fs.readFileSync("./ex.txt").toString().trim());


// 처음 풀이
// 2 or 3으로 나눈 나머지를 뺀다음 나누어 떨어지는 값을
// 횟수 구하는 함수에 넣어서 답을 구한다.
// 이 방법은 2 or 3중에 어떤 값을 선택해야 하는지에 대한 분기점을 제대로 잡지 못했다.

// const checkNum = (target, num) => {
//     let cnt = 0;
//     while (target !== 1) {
//         if (target % num !== 0) return 10 ** 6;
//         target /= num;
//         cnt++;

//     }
//     return cnt;
// }

// const threeMod = input % 3;
// const threeDiv = threeMod < input ? checkNum(input - threeMod, 3) : 10 ** 6;
// const twoMod = input % 2;
// const twoDiv = checkNum(input - twoMod, 2);

// const ans = threeMod + threeDiv < twoMod + twoDiv ? threeMod + threeDiv : twoMod + twoDiv;


// 두 번째 풀이
const DP = new Array(input + 1).fill(0);

for (let i = 2; i <= input; i++) {
    DP[i] = DP[i - 1] + 1;

    if (i % 2 === 0) {
        DP[i] = Math.min(DP[i], DP[i / 2] + 1);
    }
    if (i % 3 === 0) {
        DP[i] = Math.min(DP[i], DP[i / 3] + 1);
    }


}
console.log(DP[input]);