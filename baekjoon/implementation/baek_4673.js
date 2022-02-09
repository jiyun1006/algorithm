// 셀프 넘버

//9977 까지를 상한선

let arr = Array(10000).fill().map((v, i) => i + 1);
const sum = (arr) => {
    return arr.reduce((a, b) => a + b);
}

for (let i = 1; i <= 10000; i++) {
    i += "";
    let tmp = Number(i) + sum(i.split("").map(Number));
    if (arr.indexOf(tmp) >= 0) arr.splice(arr.indexOf(tmp), 1);

}
arr.map((i) => console.log(i));

// 두번째 풀이 (시간 단축)

let arr = Array(9999);
const sum = (arr) => {
    return arr.reduce((a, b) => a + b);
}

for (let i = 1; i <= 10000; i++) {
    i += "";
    let tmp = Number(i) + sum(i.split("").map(Number));
    arr[tmp] = true;
}

for (let i = 1; i <= 10000; i++) {
    if (!arr[i]) {
        console.log(i);
    }
}
