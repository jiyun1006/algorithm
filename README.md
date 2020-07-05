# Baekjoon

>### 2352
**Lower bound 를 이용하는 문제  (원하는 값 이상이 처음 나오는 위치)**   

**시간 복잡도를 생각해서 python 내장 라이브러리 bisect를 이용한다.** 

```
for i in range(1,n):
    if number[i] > dp[-1]:
        dp.append(number[i])
    else:
        dp[bisect(dp,number[i])] = number[i]
```



***



>### 2529
**백트래킹을 이용하는 문제**

**먼저 DFS원리로 탐색하고, 다시 백트래킹으로 탐색한다.**

```
for i in range(10):
        if not c[i]:
            if cnt == 0 or possible(s[-1], str(i), op[cnt - 1]):
                c[i] = True
                solve(cnt + 1, s + str(i))
                c[i] = False
```
