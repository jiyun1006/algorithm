const fs = require("fs");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
let input = fs.readFileSync("./ex.txt").toString().trim().split('\n');


function comb(arr, cnt) {
    const results = [];
    if (cnt === 1) return arr.map((value) => [value]);

    arr.forEach((fixed, index, origin) => {
        const rest = origin.slice(index + 1);
        const combinations = comb(rest, cnt - 1);

        const attached = combinations.map((combination) => [fixed, ...combination]);
        results.push(...attached);

    });

    return results;
}


const result = comb(input, 2);
const sum = input.map((item) => Number(item)).reduce((a, b) => a + b);

for (ansList of result) {
    const exSum = ansList.map((item) => Number(item)).reduce((a, b) => a + b);
    if (sum - exSum === 100) {
        input = input.filter((arr, idx) => !ansList.includes(arr)).join("\n");
        console.log(input);
        return;
    }
}


