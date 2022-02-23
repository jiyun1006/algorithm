// 영역 구하기

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync('./ex.txt').toString().trim().split('\n');

const [row, col, K] = input.shift().split(" ").map((el) => +el);

// 모눈종이
let graph = Array.from(new Array(row), () => Array(col).fill(false));


// 모눈종이에 영역 칠하기 (true가 칠해진 부분);
input.map((el) => {
    let [col1, row1, col2, row2] = el.split(" ").map((i, idx) => {
        if (idx % 2 === 1) return row - (+i);
        else return +i
    });

    for (let i = row2; i < row1; i++) {
        for (let j = col1; j < col2; j++) {
            if (!graph[i][j]) {
                graph[i][j] = true;
            }
        }
    }
})


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1];

const dfs = (x, y, arr) => {
    if (!arr[x][y]) {
        cnt++;
        arr[x][y] = true;
        for (let i = 0; i < 4; i++) {
            let X = dx[i] + x;
            let Y = dy[i] + y;
            if (X >= 0 && X < row && Y >= 0 && Y < col) {
                dfs(X, Y, arr);
            }
        }
    }
    return cnt;
}

let cnt = 0;
let ansList = new Array();

for (let i = 0; i < row; i++) {
    for (let j = 0; j < col; j++) {
        if (!graph[i][j]) {
            cnt = dfs(i, j, graph);
            ansList.push(cnt);
            cnt = 0;
        }
    }
}

console.log(ansList.length);
console.log(ansList.sort((a, b) => a - b).join(' '));





