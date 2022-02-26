// 촌수계산

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const n = Number(input.shift());
const [tar1, tar2] = input.shift().split(" ").map((el) => +el);
const m = Number(input.shift());
let arr = Array.from(Array(n + 1), () => Array());

input.map((el) => {
    [a, b] = el.split(" ").map((i) => +i);
    arr[a].push(b);
    arr[b].push(a);
})


const bfs = (start) => {
    const visited = new Array(n + 1).fill(-1);
    let ans = 0;
    visited[start] = 0;
    const queue = [start];

    while (queue.length) {
        ans++;
        let cur = queue.shift();
        for (let i = 0; i < arr[cur].length; i++) {
            let next = arr[cur][i];
            if (visited[next] === -1) {
                visited[next] = visited[cur] + 1;
                queue.push(next);
            }
        }
    }
    return visited;
}

const answer = bfs(tar1)

console.log(answer[tar2]);
