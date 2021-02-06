#!/usr/bin/env python
# coding: utf-8

# In[13]:


from collections import deque

N, M = map(int, input().split())

maze = [list(map(int,input())) for _ in range(N)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x , y = queue.popleft()
        
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <= -1 or ny <= -1 or nx >=N or ny>= M or maze[nx][ny] == 0:
                continue
            
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y] + 1
                queue.append((nx,ny))

    return maze[N-1][M-1]
    

print(bfs(0,0))

