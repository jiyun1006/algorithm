#!/usr/bin/env python
# coding: utf-8

# In[39]:


import heapq
N = int(input())
K = int(input())



# 보드판과 사과를 배치
board = [[0] * N for _ in range(N)]
for _ in range(K):
    row, col = map(int, input().split())
    board[row-1][col-1] = 2

# 변환 횟수    
# 우선순위 큐 활용
heap = list()
L = int(input())
for _ in range(L):
    XC = input().split()
    heapq.heappush(heap, (int(XC[0]),XC[1]))

# 제일 빨리 오는 변환 횟수 받음.
change = heapq.heappop(heap)
time = change[0]
direction = change[1]

c_dir_list = ["R", "B", "L", "U"]
c_dir = 0
c_time = 0 
distance = 1
# snake 현재 위치
snake = [0,0]
snake_list = [[0,0]]


while 1:
    c_time+=1          

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
         
    if c_dir == 0:
        snake[1] += 1
        
    elif c_dir == 1:
        snake[0] += 1
        
    elif c_dir == 2:
        snake[1] -= 1
        
    elif c_dir == 3:
        snake[0] -= 1
    
    if snake[1] >= N or snake[1] < 0 or snake[0] >= N or snake[0] < 0 or board[snake[0]][snake[1]] == 1:
        break
    
    if board[snake[0]][snake[1]] == 2:
        distance += 1
        snake_list.append([snake[0],snake[1]])
        for i in range(distance):
            board[snake_list[i][0]][snake_list[i][1]] = 1

    else:
        snake_list.append([snake[0],snake[1]])
        tmp = snake_list.pop(0)
        board[tmp[0]][tmp[1]] = 0
        for i in range(distance):
            board[snake_list[i][0]][snake_list[i][1]] = 1
        
        
    
print(c_time)

