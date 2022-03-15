// 통계학

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split('\n');
const num = Number(input.shift());
const arr = new Array();
let cntArr = {}; // 최빈값을 위한 객체

input.map((el) => {
    arr.push(+el);
    if (cntArr[el]) cntArr[el] += 1;
    else cntArr[el] = 1;
})

arr.sort((a, b) => a - b);

const ans = new Array();

// 산술평균
ans.push(Math.round(arr.reduce((a, b) => a + b) / arr.length, 1));

// 중앙값
ans.push(arr[Math.floor(arr.length / 2)]);

// 최빈값
const cntValue = Object.values(cntArr).sort((a, b) => b - a);

const max = Math.max.apply(null, (cntValue));
const cntKey = Object.keys(cntArr);
let idx = cntValue.indexOf(max);


const tmp = new Array();
while (idx !== -1) {
    let keyTmp = cntKey.find(key => cntArr[key] === cntValue[idx]);
    tmp.push(keyTmp);
    delete cntKey[cntKey.indexOf(keyTmp)];
    idx = cntValue.indexOf(max, idx + 1);
}

if (tmp.length > 1) {
    tmp.sort((a, b) => a - b);
    ans.push(Number(tmp[1]));
}
else {
    ans.push(Number(...tmp));
}


// 범위
const mx = Math.max.apply(null, arr);
const mn = Math.min.apply(null, arr);
ans.push(mx - mn);



console.log(ans.join('\n'));