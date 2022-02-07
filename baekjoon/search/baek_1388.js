const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const [N, M] = input.shift().split(' ').map(Number);

let graph = new Array();
let visited = Array.from(new Array(N), () => Array(M).fill(false));
let ans = 0;

input.map((i) => {
    const tmp = i.split('');
    graph.push(tmp);
})

df = [1, -1];

const dfs = (x, y) => {
    if (graph[x][y] === '-' && !visited[x][y]) {
        visited[x][y] = true;

        for (let i of df) {
            let dy = y + i;
            if (dy > 0 && dy < M && graph[x][dy] === '-') {
                dfs(x, dy);
            }
        }
    }
    if (graph[x][y] === '|' && !visited[x][y]) {
        visited[x][y] = true;
        for (let j of df) {
            let dx = x + j;
            if (dx > 0 && dx < N && graph[dx][y] === '|') {
                dfs(dx, y);
            }
        }
    }
}

for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
        if (!visited[i][j]) {
            dfs(i, j);
            ans += 1;
        }
    }
}

console.log(ans);