const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const [N, M] = input.shift().split(" ").map(Number);
let graph = [...new Array(N + 1)].map(() => []);
let visited = [...new Array(N + 1)].map(() => false);

// dfs 함수
const dfs = (start) => {
    visited[start] = true;
    graph[start].map((tmp) => {
        if (!visited[tmp]) {
            dfs(tmp);
        }
    })
}

// graph 생성.
input.map((tmp) => {
    let [tmp1, tmp2] = tmp.split(" ").map(Number);
    graph[tmp1].push(tmp2);
    graph[tmp2].push(tmp1);
})

// 실행 부분
let ans = 0;

for (let i = 1; i <= N; i++) {
    if (!visited[i]) {
        dfs(i);
        ans += 1;
    }
}

console.log(ans);