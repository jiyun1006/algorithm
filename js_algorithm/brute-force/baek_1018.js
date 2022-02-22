const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const [input, ...arr] = fs.readFileSync('.ex/txt').toString().trim().split('\n');
const [N, M] = input.split(" ").map((el) => +el);

//8 x 8 보드판 만드는 함수
const makeBoard = (row, col, arr) => {
    const board = arr.slice(row, row + 8).map((el) => {
        return el.split("").slice(col, col + 8);
    })
    return board;
}

// 흰색 or 검은색 먼저 체스판 확인해서 최소값 구하는 함수
const check = (arr) => {
    const color = ["BWBWBWBW", "WBWBWBWB"];
    let min = 64;
    for (let k = 0; k < 2; k++) {
        let cnt = 0;
        let tmp = k;
        for (let i = 0; i < 8; i++) {
            for (let j = 0; j < 8; j++) {
                if (arr[i][j] !== color[tmp % 2][j]) cnt++;
            }
            tmp++;
        }
        if (min > cnt) min = cnt;
    }
    return min;
}

let ans = 64;
for (let i = 0; i <= N - 8; i++) {
    for (let j = 0; j <= M - 8; j++) {
        const board = makeBoard(i, j, arr);
        let tmp = check(board);
        ans = ans > tmp ? tmp : ans; // 여러 체스판 중 최소값 찾기.
    }
}

console.log(ans);