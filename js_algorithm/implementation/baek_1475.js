// 방 번호

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const arr = input.shift().split("").map((el) => {
    if (el === '9') return 6;
    else return +el;
})

// 플라스틱 숫자 세트
const num = [0, 1, 2, 3, 4, 5, 6, 6, 7, 8];


// 플라스틱 숫자 세트의 개수를 세기위한 배열
const numArr = new Array();
numArr.push(...num);

let ans = 1;

arr.map((el) => {
    if (numArr.indexOf(el) === -1) {
        ans++;
        numArr.push(...num);
    }
    numArr.splice(numArr.indexOf(el), 1);
})

console.log(ans);