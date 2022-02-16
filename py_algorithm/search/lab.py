#!/usr/bin/env python
# coding: utf-8

# In[2]:


n, m = map(int, input().split())

lab = list()
temp = [[0]*m for _ in range(n)]

for _ in range(n):
    lab.append(list(map(int,input().split())))
    


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

def fill_vir(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx >= 0 and ny >= 0 and nx < n and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                fill_vir(nx, ny)     
def get_score():
    score = 0 
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score
        
def dfs(cnt):
    global result
    if cnt == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    fill_vir(i, j)
        result = max(result, get_score())
        return
    
    
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                cnt += 1
                dfs(cnt)
                lab[i][j] = 0
                cnt -= 1

                


dfs(0)
print(result)

