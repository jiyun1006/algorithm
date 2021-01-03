# algorithm   


# leetcode   

>### 49. anagrams 문제    
<br>

**defaultdict를 이용해서 키 값의 존재 여부 체크를 간편화할 수 있다.**   

**ana 딕셔너리는 같은 문자를 가진 문자열을 키 값으로 하고, 해당되는 문자열을 넣는다.**   

<br>

```py
ana = collections.defaultdict(list)
        
        for word in strs:
            ana[''.join(sorted(word))].append(word)
        return ana.values()
```


<br>
<br>

>### 5. longest palindrome 문제
<br>

**Palindrome을 짝수의 경우와 홀수의 경우로 나눠서 구한다.**   

**반복문을 써서 전체 문자열을 순회하며, 제일 긴 회문을 찾는다.**   

**'왼쪽 포인터는 0이상, 오른쪽 포인터는 문자열의 길이 -1 이하'의 조건을 만족해야 한다.**    

**위의 조건을 만족하는 문자열 중, 양 끝이 같은 문자열을 찾는다.(짝, 홀 동일한 함수 가능)**


<br>

```py
def longestPalindrome(s: str) -> str:
 
        def check(left: int, right: int, strs: list[str]) -> list[int]:
            while left >= 0 and right <= len(strs) -1 and strs[left] == strs[right]:
                left -= 1
                right += 1
            return strs[left+1 : right]
    
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        ans =''
        for i in range(len(s)):
            ans = max(ans, check(i,i+1,s), check(i,i+2,s),key =len)
            
        return ans
```

<br>
<br>

>### 42. Trapping Rain Water 문제

<br>

**왼쪽에서 오른쪽으로 가면서 변곡점을 만났을 때, 빗물의 양을 더해간다**   

**모든 테스트 케이스에 대응하려다 보니, 코드가 길어지고 지저분해졌고, 모든 답을 구하는데 실패했다.**   

<br>

```py
if len(height) > 1:
            i, ans, temp, cnt = 0, 0, 0, 0
            left, max_temp = [], (0,0)

            while i != len(height):
                if height[i] == 0:
                    i += 1
                    cnt += 1
                    continue
                if left:
                    cnt += 1
                    if height[i] >= left[0][0] and cnt >= 2:
                        ans += ((i - left[0][1] - 1) * (left[0][0]) - temp)
                        temp = 0
                        left.pop()
                        left.append((height[i], i))
                        i += 1
                        cnt = 0
                    else:
                        temp += height[i]
                        max_temp = max(max_temp, (height[i], i))
                        i += 1

                else:
                    left.append((height[i], i))
                    i += 1
                    
                    ............<생략>
                    
```

<br>

**투 포인터를 이용해서 양쪽을 비교하는 방법**   

**왼쪽의 max지점과 오른쪽의 max지점을 비교해서 물의 양을 구한다. (한쪽의 max가 더 크면, 최종적으로 어차피 더해질 빗물의 양이다.)**   

```py
 if not height:
            return 0
        left, right = 0, len(height)-1
        l_max, r_max = height[left], height[right]
        ans = 0
        while left <= right:
            l_max, r_max = max(l_max, height[left]), max(r_max, height[right])
            if l_max <= r_max:
                ans += l_max - height[left]
                left += 1
            else:
                ans += r_max - height[right]
                right -= 1
```

<br>
<br>


>## 238. Product of Array Except Self   
<br>

**자기자신을 제외한 왼쪽의 곱과 오른쪽의 곱을 곱하는 방법 --> O(n)으로 풀기위해서**   


<br>

*왼쪽 곱 1  1(1)  2(1x2)  6(1x2x3)*   

<br>

*오른쪽 곱 1  4(4)  12(3x4)  24(2x3x4)*   

<br>

```py
 a = 1
        temp = []
        for i in nums:
            temp.append(a)
            a*=i
        a = 1
        
        for j in range(len(nums), 0, -1):
            temp[j-1]*=a
            a*=nums[j-1]
        return temp
```

<br>
<br>


>## 234.Palindrome Linked List 
<br>

**연결리스트의 회문을 구하는 문제이다.**   

*ListNode의 클래스*   

<br>

```py
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
```

<br>

**기본적인 리스트의 성질을 이용해서 풀어낸다.(deque를 이용해서 pop(n)의 시간복잡도를 줄인다.)**   
<br>

```py
temp_list: Deque = deque()
        
        if not head:
            return True
        
        node = head
        
        while node is not None:
            temp_list.append(node.val)
            node = node.next
        
        while len(temp_list) > 1:
            if temp_list.pop() != temp_list.popleft():
                return False
        return True
```
<br>

**연결리스트 회문 풀이법의 올바른 접근은 러너(Runner)기법이다.**   

**빠른 러너와 느린 러너를 이용해서 각각, 연결리스트의 끝과, 역순을 저장하는데 이용한다.**    

<br>

*slow가 지나온 길을 rev에 저장하면서 역순으로 저장하게끔 한다.*   

<br>
   
```py
fast = slow = head
        rev = None
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev
```
<br>
<br>

>## 39. Combination Sum  
<br>

**더하는 숫자가 중복이 되도 되므로, 전체 배열을 반복하도록 한다.**    

**dfs를 진행하면서, target 숫자를 넘어가면 해당 트리는 그만 진행한다.**   

**또한 같은 배열이 답에 포함되지 않도록, 정렬을 이용한다.**   

<br>

```py
def DFS(ans: int, strs: List):
            if ans > target:
                return 
            
            if ans == target:
                strs = sorted(strs)
                if strs in ans_list:
                    return
                ans_list.append(strs)
                
            
            for i in range(len(candidates)):
                temp  = strs[:]  // temp = strs 이라 쓰게 되면 참조된 값이 같게 되어 제대로 
                temp.append(candidates[i])
                DFS(ans + candidates[i], temp)
        
        DFS(ans, strs)
        return ans_list
```
 
<br>
<br>


>## 787.Cheapest Flights Within K Stops   

<br>

**기존의 다익스트라 알고리즘을 이용한다. (제한 조건 때문에, 약간의 변형이 필요함.)**   

**우선순위 큐를 이용해서 최솟값을 구한다.(움직이는 횟수가 정해져 있으므로, 도착점에 도착했는지에 대한 확인 필요.)**   

<br>

```py
q = [(0, src, K)]
            
        while q:
            p, node, k = heapq.heappop(q)
            
            # 목표지점에 도착했을 때, 비용을 결과값으로 내보낸다.
            if node == dst:
                return p
                
            # 정점을 하나 지날 때 마다, 움직이는 횟수를 1씩 뺀다.    
            # k가 0미만이면, 중단.
            if k >= 0:
                for a, b in dic[node]:
                    t = p + b
                    heapq.heappush(q, (t, a, k-1))
```

<br>
<br>

>## 543.Diameter of Binary Tree    

<br>

**이진 트리에서 두 노드 간 가장 긴 경로의 길이를 구하는 문제이다.**   

**리프노드에서부터 부모노드로 역순으로 올라가면서 길이를 더해가면 해결된다.**   

<br>

```py
def dfs(node: TreeNode):
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # 가장 긴 경로를 더한다. (왼쪽,오른쪽 사이의 경로이므로 +2)
            self.longest = max(self.longest, (left+right+2))
            
            # 리프노드부터 올라가면서 값을 만들어간다.
            return max(left, right) + 1
```

<br>
<br>



*****
*****
*****  

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

```py
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

```py
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

```py
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
```py
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


```py
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

```py
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

```py
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
```py
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
```py
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
```py
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
```py
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
   
```py
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
   
```py
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
   
   
```py
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
   
```py
temp = sorted(int(sys.stdin.readline()) for _ in range(N))

# enumerate 사용
sum_list = sum(abs((i+1)- value) for i , value in enumerate(temp))
print(sum_list)
```   
   
*처리속도가 줄어드는 것을 볼 수 있다.*
