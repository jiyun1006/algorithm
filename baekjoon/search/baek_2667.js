const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const N = Number(input.shift());
let graph = new Array();

// graph 생성
input.map((i) => {
    const tmp = i.split('');
    graph.push(tmp);
})

// dfs 함수를 위한 좌표 이동 객체
const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];
let cnt = 0;


// dfs 함수
const dfs = (x, y) => {
    if (graph[x][y] === '1') {
        cnt += 1;
        graph[x][y] = '0';
        for (let i = 0; i < 4; i++) {
            let X = x + dx[i];
            let Y = y + dy[i];
            if (X >= 0 && X < N && Y >= 0 && Y < N) {
                dfs(X, Y);
            }
        }
    }
    return cnt;
}


let ans = 0;
let ansList = new Array();

for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
        if (graph[i][j] === '1') {
            ans = dfs(i, j);
            ansList.push(ans);
            cnt = 0; // 새로운 집 군락을 위한 초기화
        }
    }
}

console.log(ansList.length);
ansList.sort((a, b) => a - b);
ansList.map((tmp) => console.log(tmp));