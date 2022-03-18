// 그림

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const [matrix, ...input] = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const [n, m] = matrix.split(" ").map((el) => +el);

const arr = input.map((el) => {
    return el.split(" ").map((i) => +i);
});


const dx = [1, -1, 0, 0];
const dy = [0, 0, 1, -1];
const bfs = (x, y) => {
    const queue = [[x, y]];
    arr[x][y] = 0;
    let cnt = 1;
    while (queue.length) {
        let ma = queue.shift();
        for (let i = 0; i < 4; i++) {
            let X = ma[0] + dx[i];
            let Y = ma[1] + dy[i];
            if (X < n && X >= 0 && Y < m && Y >= 0) {
                if (arr[X][Y] === 1) {
                    arr[X][Y] = 0;

                    queue.push([X, Y]);
                    cnt++;
                }
            }
        }
    }
    return cnt;
}

let ans = 0;
let ansMax = 0;
let tmp = 0;
for (let i = 0; i < n; i++) {
    for (let j = 0; j < m; j++) {
        if (arr[i][j] === 1) {
            tmp = bfs(i, j);
            ansMax = ansMax < tmp ? tmp : ansMax;
            ans++;
        }

    }
}

console.log(ans + "\n" + ansMax);