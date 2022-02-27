// 효율적인 해킹

const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const len = input.shift().split(" ").map((i) => +i)[0];
const arr = Array.from(Array(len + 1), () => Array());
input.map((el) => {
    [end, start] = el.split(" ").map((i) => +i);
    arr[start].push(end);
})

const search = (start) => {
    const visited = new Array(len + 1);
    visited[start] = true;
    let queue = [start];

    while (queue.length) {
        let cur = queue.shift();
        for (let i = 0; i < arr[cur].length; i++) {
            let next = arr[cur][i];
            if (!visited[next]) {
                visited[next] = true;
                queue.push(next);
            }
        }
    }
    return visited;

}


const ans = new Array(len + 1);
for (let i = 0; i <= len; i++) {
    ans[i] = search(i).filter((el) => el === true).length;
}

const max = Math.max.apply(null, ans);
let idx = ans.indexOf(max);

let result = "";
while (idx !== -1) {
    result += idx + " ";
    idx = ans.indexOf(max, idx + 1);
}
console.log(result.trim());