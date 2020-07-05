Baekjoon
-------------------
>### 2352
**Lower bound 를 이용하는 문제이다.  (원하는 값 이상이 처음 나오는 위치)**   

**시간 복잡도를 생각해서 python 내장 라이브러리 bisect를 이용한다.** 

```
for i in range(1,n):
    if number[i] > dp[-1]:
        dp.append(number[i])
    else:
        dp[bisect(dp,number[i])] = number[i]
```


