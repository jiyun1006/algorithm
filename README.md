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
   
   
----------------------------           
   
   

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
   
   
----------------------------           
   
   

>### 2437
**처음 시도**  

**combinations 이용해서 계수정렬 형식으로 시도**   

```
for i in range(1, N):
    weg = list(set(list(combinations(weight, i))))

    for j in range(len(weg)):
        if value[sum(weg[j])] != 0:
            continue
        else:
            value[sum(weg[j])] += 1

```
*메모리 초과로 인한 리스트 인덱스 범위 초과*   





**두 번째 시도**   

**bisect를 이용해서 무게들의 더해가면서 그보다 1 큰 값**   
```
for i in range(N):
    value = sum_list[i]
    weight_copy = weight.copy()
    while value > 0:
        value -= weight_copy[bisect(weight_copy, value) - 1]
        weight_copy.pop(bisect(weight_copy, value) - 1)
        if not weight_copy:
            break
    if value < 0:
        print(sum_list[i])
        break
```

*while문 break 조건 부족으로 오류*

    

               
   

**세 번째 시도**   

**(더해가는 값+1)이 리스트에 있는 값보다 작을 때 반복문 탈출**   


```
weight.sort()
sum = 0
for i in range(N):
    if sum + 1 >= weight[i]:
        sum += weight[i]
    else:
        break
print(sum+1)
```
