const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const dx = [1, 1, 1, -1, -1, -1, 0, 0];
const dy = [1, -1, 0, 1, -1, 0, 1, -1];

const dfs = (x, y, row, col, graph) => {
    if (graph[x][y] === 1) {
        graph[x][y] = 0
        for (let i = 0; i < 8; i++) {
            let X = x + dx[i];
            let Y = y + dy[i];
            if (X >= 0 && X < row && Y >= 0 && Y < col) {
                dfs(X, Y, row, col, graph);
            }
        }
    }
}

while (true) {
    let ans = 0;
    let [col, row] = input.shift().split(" ").map(Number);
    if (col === 0 && row === 0) break;
    let graph = [...new Array(row)];
    for (let i = 0; i < row; i++) {
        let mat = input.shift().split(" ").map(Number);
        graph[i] = mat;
    }
    for (let i = 0; i < row; i++) {
        for (let j = 0; j < col; j++) {
            if (graph[i][j] === 1) {
                dfs(i, j, row, col, graph);
                ans++;
            }
        }
    }
    console.log(ans);
}
