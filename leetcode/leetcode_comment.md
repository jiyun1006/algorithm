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
