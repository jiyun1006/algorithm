const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let [N, ...arr] = fs.readFileSync('./ex.txt').toString().trim().split('\n');

N = +N;
arr = arr.map((el) => el.split(" ").map(i => +i));

for (let i = 1; i < N; i++) {
    arr[i][0] += Math.min(arr[i - 1][1], arr[i - 1][2]);
    arr[i][1] += Math.min(arr[i - 1][0], arr[i - 1][2]);
    arr[i][2] += Math.min(arr[i - 1][0], arr[i - 1][1]);
}

console.log(Math.min.apply(null, arr[N - 1]));
