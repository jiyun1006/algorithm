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
const bfs = (start, tar) => {
    const visited = new Array(n + 1);
    visited[start] = true;
    let ans = 0;
    const queue = [start];

    while (queue.length) {
        const cur = queue.shift();
        ans++;
        for (let i = 0; i < arr[cur].length; i++) {
            let next = arr[cur][i];
            if (!visited[next]) {
                if (next === tar) return ans;
                visited[next] = true;
                queue.push(next);
            }
        }
    }
    return -1;
}

const abs = bfs(7, 3);
console.log(abs);