// 안전 영역
const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const N = Number(input.shift());
let graph = [];
let max = 0;

input.map((el) => {
    let tmp = el.split(" ").map(Number);
    graph.push(tmp);

    // 지역 내의 최고 높이 구하는 코드
    tmpMax = Math.max.apply(null, tmp);
    max = Math.max(tmpMax, max);
})

// 상하좌우만 이어졌을 때 땅으로 인정.
const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];

// dfs 함수
const dfs = (visited, start, x, y) => {
    if (!visited[x][y] && graph[x][y] > start) {
        visited[x][y] = true;
        for (let i = 0; i < 4; i++) {
            let X = x + dx[i];
            let Y = y + dy[i];
            if (X >= 0 && X < N && Y >= 0 && Y < N) {
                dfs(visited, start, X, Y);
            }
        }
    }
}

// 물 높이에 따라 구해지는 지역 개수 담아둘 객체
let ansList = [];

// max의 높이까지 모든 물 높이를 구해본다.
for (let i = 0; i <= max; i++) {
    let ans = 0;
    let visited = Array.from(new Array(N), () => new Array(N).fill(false));
    for (let j = 0; j < N; j++) {
        for (let k = 0; k < N; k++) {
            if (!visited[j][k] && graph[j][k] > i) {
                dfs(visited, i, j, k);
                ans++;
            }
        }
    }
    ansList.push(ans);
}
console.log(Math.max.apply(null, ansList));