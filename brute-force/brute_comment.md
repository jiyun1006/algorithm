# Brute_force   

<br>

## 문제 해설(내 풀이, 정답 풀이)

<br>

>## 게임 개발   

<br>

**N,M의 행렬에서 움직이는 캐릭터를 조작하는 문제**   

**특별한 알고리즘 없이 구현 위주로 품.**   

<br>

```python
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]    ---> 방향을 위해 미리 설정하면, 코드가 깔끔해짐.

while 1:
    if mp[row][col] == '0':  
        mp[row][col] = '1'     ----> 반복문안에서 행렬을 돌아다니며, 0이면 표시를 위해 1로 바꿈.
        
    turn_lf()    ---> 문제 조건에 따라 먼저 회전(따로 함수 만듬)
    
    tmp_x = row + dx[d]
    tmp_y = col + dy[d]    ---> 임의의 x,y에 방향대로 움직인 값 설정.
    
    if mp[tmp_x][tmp_y] != '1':   ---> 처음 가 본 방향이 1이 아니라면, 이동 횟수를 늘리고, 다시 방향탐색
        cnt += 1
        row = tmp_x
        col = tmp_y
        turn_cnt = 0
        continue
        
        
    else:   ---> 1이라면, turn한 횟수 늘리고, 다시 처음으로
        turn_cnt += 1
        
    if turn_cnt == 4:  ---> 4방향 모두 봤을 때, 갈 곳이 없으면, 뒤로
        tmp_x = row - dx[d]
        tmp_y = col - dy[d]
        
        if mp[tmp_x][tmp_y] == 0:
            row = tmp_x
            col = tmp_y
        
        else:   ---> 뒤로 못가면 반복 파괴.
            break
        turn_cnt = 0

```

*****

<br>
<br>

>## 문자열 압축(2020카카오)   

<br>

- 내가 푼 풀이   

<br>

**python for문에서 반복 단위를 늘려가며 단위마다의 줄어드는 길이 확인**   

**얼만큼 줄어드는지에 대한 잘못된 코드로, 답이 안나옴**   

```python
for j in range(1,length+1):
    idx, cnt = 0, 0
    tmp = ''
    cnt2 = 1   ---> 반복 횟수를 저장하는 변수
    for i in range(0, len(s)+1, j):
        if tmp != s[idx:i]:
            if tmp and cnt2 > 1:   ---> 2번 이상 반복되었다면, 실행
                cnt += j*(cnt2-1)-1  ---> 압축을 해서 줄어드는 길이를 저장하는 변수
          
                cnt2 = 1
        if tmp == s[idx:i]:
            cnt2 += 1
        tmp = s[idx:i]
        idx = i   

    if cnt2 > 1:     ----> 남은 문자열 중, 줄어드는 길이 저장.
        cnt += j*(cnt2-1)-1            
    cnt_list.append(cnt)
```   

<br>

- 풀이   

**알고리즘 자체는 동일하나, 문자열 자체를 저장함으로써 줄어드는 길이에 대한 복잡함 해소.**   

```python
for j in range(1,length+1):
    idx, cnt = 0, 1
    tmp = s[0:j]
    tmp2 = ''
    for i in range(j, len(s), j):
        if tmp == s[i:i+j]:
            cnt += 1    ---> 반복횟수 기록.
        else:
            tmp2 += str(cnt) + tmp if cnt >= 2 else tmp     ---> 반복횟수가 2회 이상이면, 해당 문자열 저장.
            tmp = s[i:i+j]
            cnt = 1

    tmp2 += str(cnt) + tmp if cnt >= 2 else tmp   ---> 남은 문자열 처리
    answer = min(answer, len(tmp2))
```
*****

<br><br>

>## 자물쇠와 열쇠 (2020카카오)   
>처음에 문제를 보고 적당한 구현 알고리즘을 떠올리지 못했다. 따라서 다른 사람의 알고리즘을 보고, 구현을 시도했다.   
>아직 완전탐색 문제들에 대한 경험 부족으로, 다양한 구현방법이 숙지가 안됨.   

<br>  

**기본적으로 문제에서 제공하는 자물쇠와 열쇠의 크기가 작기 때문에, 완전탐색으로 모든 리스트를 접근할 수 있다.   
(앞으로 시간복잡도, 공간복잡도에 대한 감을 키워야 할 듯.)**   

**또한 key의 원소를 이동시키는 것과 lock 리스트에 패딩을 줘서 더 넓은 범위에서 이동하는 행위가 같다.**   

**따라서 따로 만들 함수는 lock이 모두 1인지와, key를 90도 회전 시키는 함수이다.**   

<br>
 
*key를 90도 회전 시키는 함수*   
```python
def rotate(key):
    n = len(key)
    m = len(key[0])
    new_list = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            new_list[i][j] = key[n-1-j][i]
    return new_list
```    

<br>

*lock이 1인지 확인하는 함수*   
```python
def check(lock):
    n = len(lock)
    m = len(lock[0])
    length = n//3

    for i in range(length, length*2):
        for j in range(length, length*2):
            if lock[i][j] != 1:
                return False
    return True
```    
<br>

*main 함수*    
```python
def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(lock[0])

    big_lock = [[0]*3*n for _ in range(m*3)]  ---> padding 생성
    for i in range(n):
        for j in range(m):
            big_lock[i+n][j+n] = lock[i][j]    ---> padding을 포함한 list에 lock 넣기.

    for _ in range(4):
        key = rotate(key)
        for i in range(n*2):
            for j in range(n*2):
                for x in range(len(key)):
                    for y in range(len(key[0])):
                        big_lock[i+x][j+y] += key[x][y]  ---> padding에도 값을 더하고, lock부분에도 값을 더한다.
                if check(big_lock):
                    return True
                for x in range(len(key)):
                    for y in range(len(key[0])):
                        big_lock[i+x][j+y] -= key[x][y]   ---> 잘못된 key라면 더했던 값 빼기

    return answer
```

*****

<br><br>

>## 뱀 (백준 3190번)   
>시뮬레이션 문제 유형으로, 문제 조건에 따라서 구현만 하면 된다.
>문제는 맞았지만, 중간중간 구현 내용을 따로 함수로 만들면 가독성을 높일 수 있을 것 같다.
>여러 문제를 풀면서, 구현에 대한 감이 생기는 중.   
 
<br>

**먼저 뱀이 지나다닐 보드판을 길이에 맞춰서 만든다. 그 다음에, 사과를 미리 보드판에 넣어둔다.**   

**뱀의 진행방향에 유의하며, 게임을 진행한다.**   

<br>

- 내가 푼 풀이   

<br>

```python
import heapq
N = int(input())
K = int(input())



# 보드판과 사과를 배치 (사과를 숫자 2로 나타낸다.)   
board = [[0] * N for _ in range(N)]
for _ in range(K):
    row, col = map(int, input().split())
    board[row-1][col-1] = 2


# 변환 조건 (시간, 방향)    
# 우선순위 큐 활용
heap = list()
L = int(input())
for _ in range(L):
    XC = input().split()
    heapq.heappush(heap, (int(XC[0]),XC[1]))


# 제일 빨리 오는 변환 횟수 받음.(우선순위 큐의 heappop을 이용해서 제일 낮은 시간을 빼낸다.)
change = heapq.heappop(heap)
time = change[0]
direction = change[1]


# 방향 설정 (index로 방향을 설정할 수 있게)
c_dir_list = ["R", "B", "L", "U"]
c_dir = 0  ---> 초기 방향 0 ("R")
c_time = 0 
distance = 1


# 뱀머리의 현재 위치
snake = [0,0]

# 뱀의 길이에 따라 차지하고 있는 보드 위치
snake_list = [[0,0]]


while 1:
    # 반복을 시작하고 바로 시간을 늘린다.
    c_time+=1          
    

    # 현재시간 - 1 과 방향 전환 시간이 같다면, 방향을 바꾼다.
    if c_time-1 == time:
        if direction == "L":
            c_dir -= 1
            if c_dir <= -1:
                c_dir = 3

        else:
            c_dir += 1
            if c_dir >= 4:
                c_dir = 0
        
        if heap:
            change = heapq.heappop(heap)
            time = change[0]
            direction = change[1]
    
    
    #진행방향에 따라 다르게 진행
    if c_dir == 0:
        snake[1] += 1
        
    elif c_dir == 1:
        snake[0] += 1
        
    elif c_dir == 2:
        snake[1] -= 1
        
    elif c_dir == 3:
        snake[0] -= 1
    
    
    #보드판을 벗어나거나, 뱀이 이미 차지하고 있는 부분이면, 반복문 파괴
    if snake[1] >= N or snake[1] < 0 or snake[0] >= N or snake[0] < 0 or board[snake[0]][snake[1]] == 1:
        break
    
    #사과에 도착하면, 길이를 늘리고, 차지하고 있는 자리 추가.
    if board[snake[0]][snake[1]] == 2:
        distance += 1
        snake_list.append([snake[0],snake[1]])
        for i in range(distance):
            board[snake_list[i][0]][snake_list[i][1]] = 1


    #사과가 아닌 빈땅에 도착하면, 뱀의 꼬리부분이 차지하고 있던 부분을 뺀다. 
    else:
        snake_list.append([snake[0],snake[1]])
        tmp = snake_list.pop(0)
        board[tmp[0]][tmp[1]] = 0
        for i in range(distance):
            board[snake_list[i][0]][snake_list[i][1]] = 1
        
        
    
print(c_time)
```


