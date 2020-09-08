# Leetcode   

### **dataclass(데코레이션)**   
<img src ="https://user-images.githubusercontent.com/52434993/92444719-4166fb80-f1ee-11ea-809d-a5c76a9da0a2.jpg" width = "60%">
<br>

### **타입 힌트**
<img src ="https://user-images.githubusercontent.com/52434993/92444722-42982880-f1ee-11ea-8187-2d2e3ae2b89e.jpg" width = "60%">
<br>

### **제네레이터**
<img src ="https://user-images.githubusercontent.com/52434993/92444724-4330bf00-f1ee-11ea-9c48-51bb932e5fc0.jpg" width = "60%">
<br>

<br><br><br>




# Baekjoon   

   
## 처리속도     
>### sys 이용하기   

>### sys.stdin.readline을 가지는 변수 생성   

>### 리스트는 미리 크기대로 생성하기.   

>### map은 리스트 만들 때 다같이 하지 않고, 따로 하기.   

*****
*****
*****   

## 문제

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

   
   
----------------------------           
   
   

>### 1700   
**처음 시도**   
   
**구멍이 비어있으면 계속 꽂는다. 다 찼다면 그 이후의 순서를 봐서 제일 빈도수가 낮은 번호를 뺀다.**   

```
stack = []
    for i in range(K):
        if hole[i] in stack:
            continue
        else:
            if len(stack) >= N:
                min_num = K
                for j in stack:
                    if hole[i:].count(j) == 0:
                        value = j
                        break
                    elif min_num > hole[i:].count(j):
                        min_num = hole[i:].count(j)
                        value = j
                stack.remove(value)
                stack.append(hole[i])
                cnt += 1
            else:
                stack.append(hole[i])
```
   
*이렇게 하면 다음에 나오는 순서가 고려가 안되므로 최소값이 구해지지 않는다.*

   





**두 번째 시도**   

**그 이후의 빈도수가 아니라 빈도가 0이 아니라면 가장 나중에 나오는 수를 뺀다(빈도가 같을 시)**   

```
stack = []
    for i in range(K):
        if hole[i] in stack:
            continue
        else:
            if len(stack) >= N:
                min_num = 0
                for j in stack:
                    if hole[i:].count(j) == 0:
                        value = j
                        break
                    elif min_num < hole[i:].index(j):
                        min_num = hole[i:].index(j)
                        value = j
                stack.remove(value)
                stack.append(hole[i])
                cnt += 1
            else:
                stack.append(hole[i])
```

   
   
----------------------------           
   
   

>### 1202   
**처음 시도**   

**가방 무게보다 작은 기준으로 정렬을 해서 그 중 최댓값 구하기**
```
for i in range(K):
    temp = sorted(J, key=lambda x: -x[:][1] if x[:][0] <= weight[i] else 1)
    print(temp)
    if weight[i] < J[0][0]:
        continue
    else:
        sum_w += temp[0][1]
        J.remove(temp[0])
```     
*처리 시간 초과*   


**두 번째 시도**   

**최소 힙 정렬을 이용해서 가방 무게보다 작은 것들을 힙에 담아서 그중 최솟값 뽑기(처리 시간 단축 목적)**   
```
for i in range(K):
    min_w = heapq.heappop(W)
    while J and min_w >= J[0][0]:
        [a, b] = heapq.heappop(J)
        heapq.heappush(sum_v, -b)

    if sum_v:
        sum_value -= heapq.heappop(sum_v)
    elif not J:
        break
```
*단순히 내장 정렬함수를 쓸 것이 아니라 힙을 사용*
      
      

   
   
----------------------------           
   
   

>### 3109   
**처음 시도**   
   
**백트래킹을 이용하는 문제이다.**
```
    if i == -1 or i == R:
        return
    if M[i][j] == 'x':
        return
    
    if j == (C - 1):
        cnt += 1
        end = True
        return

    for k in i_list:
        pipe(i + k, j + 1)
        if end:
            return
```   
*한 번 지나간 자리에 대한 처리를 안해서 예상보다 많은 결과값이 나온다.*   
   
**두 번째 시도**   
   
**한 번 지나간 자리는 'x'로 바꿔서 같은 길을 들어가지 않게 한다**   
```
    if i == -1 or i == R:
        return
    if M[i][j] == 'x':
        return
    M[i][j] = 'x'
    
    if j == (C - 1):
        cnt += 1
        end = True
        return

    for k in i_list:
        pipe(i + k, j + 1)
        if end:
            return
```
*같은 루트를 지나는 오류 해결*   

     

   
   
----------------------------           
   
   

>### 9576   
**리스트에 책의 번호를 다 넣고 제거하는 방식으로 하면 처리속도가 너무 느림**   
   
**문제에서 제시한 처리속도를 초과하지는 않지만 비효율적**   
   
```
    for i in range(1, N + 1):
        N_list.append(i)

    cnt = 0
    for i in range(M):
        for j in range(num[i][0], num[i][1] + 1):
            if j in N_list:
                N_list.remove(j)
                cnt += 1
                break
```   
*위의 코드에서 N_list에 미리 0을 넣고 범위를 지정해서 효율적으로 코드 바꿈.*   
   
```
N_list = [0] * (N + 1)

    for i in range(M):
        for j in range(num[i][0], num[i][1] + 1):
            if N_list[j] == 0:
                N_list[j] = 1
                break
```   
*처리속도가 확연히 줄어든 것을 확인할 수 있음.*    

     

   
   
----------------------------           
   
   

>### 2012   
**번호를 넣는 순서와 해당 숫자의 차이를 구하면 된다.**   
   
   
```
for i in range(N):
    a = int(sys.stdin.readline())
    temp[i] = a
temp.sort()
temp2 = [0] * N

for i in range(1, N + 1):
    temp2[i-1] = abs(temp[i-1] - i)

print(sum(temp2))
```   
**enumerate를 사용하면 더 효율적이게 바꿀 수 있다.**   
   
```
temp = sorted(int(sys.stdin.readline()) for _ in range(N))

# enumerate 사용
sum_list = sum(abs((i+1)- value) for i , value in enumerate(temp))
print(sum_list)
```   
   
*처리속도가 줄어드는 것을 볼 수 있다.*






