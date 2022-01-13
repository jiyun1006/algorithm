const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : './ex.txt';
let input = fs.readFileSync("./ex.txt").toString().split('\n');

const NM = input.shift().split(" ").map(Number);
const N = NM.shift();
const M = NM.shift();

const num = input.shift().split(" ").map(Number);

let arr = new Array(N);
arr.fill(false, 0, N);


let min = 300000;
let sum = 0;
let answer = 0;

solution(3, 0);
console.log(answer);

function solution(last, start) {
    if (last === 0) {
        if (sum <= M && M - sum < min) {
            min = M - sum;
            answer = sum;
        }
        return;
    }

    for (let i = 0; i < num.length; i++) {
        if (!arr[i]) {
            arr[i] = true;
            sum += num[i];
            solution(last - 1, i);
            console.log(min);
            arr[i] = false;
            sum -= num[i];
        }
    }
}