// 트리의 부모 찾기

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const num = Number(input.shift());

let arr = Array.from(new Array(num + 1), () => new Array());

input.map((el) => {
    let [a, b] = el.split(" ").map((i) => +i);
    arr[a].push(b);
    arr[b].push(a);
})


const bfs = (start) => {
    const answer = [];
    const visited = new Array(num + 1);
    visited[start] = true;

    const queue = [start];

    while (queue.length) {
        const cur = queue.shift();
        for (let i = 0; i < arr[cur].length; i++) {
            const next = arr[cur][i];
            if (!visited[next]) {
                visited[next] = true;
                answer[next] = cur;
                queue.push(next);
            }
        }
    }
    return answer;
}

const queue = bfs(1);
let ans = "";
queue.map((el) => { ans += el + "\n" });
console.log(ans);

