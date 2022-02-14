const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');
const T = Number(input.shift());


// graph 채우는 함수
const fillGraph = (input, graph) => {
    input.map((tmp) => {
        const [x, y] = tmp.split(" ").map(Number);
        graph[x][y] = 1;

    })
    return graph;
}

// 전체 graph만드는 함수
const makeGroup = (M, N, input) => {

    let graph = Array.from(new Array(M), () => new Array(N).fill(0));
    graph = fillGraph(input, graph);
    return graph;
}


// dfs 함수 
const dfs = (M, N, x, y, graph) => {

    if (graph[x][y] === 1) {
        cnt += 1;
        graph[x][y] = 0;
        for (let i = 0; i < 4; i++) {
            let X = dx[i] + x;
            let Y = dy[i] + y;
            if (X >= 0 && X < M && Y >= 0 && Y < N) {
                dfs(M, N, X, Y, graph);
            }
        }
    }
    return cnt;
}

const graphDfs = (M, N, graph) => {
    let ansList = new Array();
    for (let i = 0; i < M; i++) {
        for (let j = 0; j < N; j++) {
            if (graph[i][j] === 1) {
                ans = dfs(M, N, i, j, graph);
                ansList.push(ans);
                cnt = 0;
            }
        }
    }
    return ansList;
}


//실행 코드

dx = [1, -1, 0, 0];
dy = [0, 0, 1, -1];
let cnt = 0;

for (let t = 0; t < T; t++) {
    const [M, N, K] = input.shift().split(" ").map(Number);
    let tInput = new Array();
    for (let k = 0; k < K; k++) {
        tInput.push(input.shift());
    }
    graph = makeGroup(M, N, tInput);
    const ans = graphDfs(M, N, graph);
    console.log(ans.length);
}
