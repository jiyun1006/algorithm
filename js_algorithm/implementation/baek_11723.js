// 집합

const fs = require("fs");
const { PassThrough } = require("stream");
const filepath = process.platform === 'linux' ? '/dev/stdin' : '.ex/txt';
const input = fs.readFileSync("./ex.txt").toString().trim().split('\n');

const num = input.shift();

let S = new Array();

const indexCheck = (number) => {
    if (S.indexOf(+number) === -1) {
        return true;
    } else return false;
}

const check = (word, number) => {
    if (word === "add") {
        if (indexCheck(number)) {
            S.push(+number);
        }
    } else if (word === "remove") {
        if (!indexCheck(number)) {
            S.splice(S.indexOf(+number), 1);
        }
    } else if (word === "toggle") {
        if (indexCheck(number)) {
            S.push(+number);
        } else {
            S.splice(S.indexOf(+number), 1);
        }
    } else if (word === "all") {
        S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 18, 20];
    } else if (word === "empty") {
        S = [];
    } else {
        if (indexCheck(number)) {
            console.log(0);
        } else {
            console.log(1);
        }
    }


}

input.map((el) => {
    const [be, af] = el.split(' ');
    check(be, af);
})


