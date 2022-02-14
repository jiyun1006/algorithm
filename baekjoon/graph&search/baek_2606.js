const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

let num1 = Number(input.shift());
let num2 = Number(input.shift());

let graph = [...new Array(num1 + 1)].map(() => []);
let visited = [...new Array(num1 + 1)].map(() => false);

let ans = -1;

const dfs = (start) => {
    graph[start].map((tmp) => {
        if (!visited[tmp]) {
            visited[tmp] = true;
            ans += 1;
            dfs(tmp);
        }
    })
}

input.map((i) => {
    const [st, de] = i.split(' ').map((tmp) => Number(tmp));
    graph[st].push(de);
    graph[de].push(st);
})

dfs(1);
console.log(ans);
