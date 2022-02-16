#!/usr/bin/env python
# coding: utf-8

# In[12]:


N, M = map(int,input().split())

row, col, d = map(int,input().split())

mp = list()
for i in range(N):
    tmp = input().split()
    mp.append(tmp)
        
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_lf():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1 
turn_cnt = 0
        
while 1:
    if mp[row][col] == '0':
        mp[row][col] = '1'
    turn_lf()   
    tmp_x = row + dx[d]
    tmp_y = col + dy[d]
    
    if mp[tmp_x][tmp_y] != '1':
        cnt += 1
        row = tmp_x
        col = tmp_y
        turn_cnt = 0
        continue
    else:
        turn_cnt += 1
        
    if turn_cnt == 4:
        tmp_x = row - dx[d]
        tmp_y = col - dy[d]
        
        if mp[tmp_x][tmp_y] == 0:
            row = tmp_x
            col = tmp_y
        
        else:
            break
        turn_cnt = 0

print(cnt)
        
    
    
   
    
        

