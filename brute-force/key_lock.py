#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(lock[0])
    
    big_lock = [[0]*3*n for _ in range(m*3)]
    for i in range(n):
        for j in range(m):
            big_lock[i+n][j+n] = lock[i][j]
    
    for _ in range(4):
        key = rotate(key)
        for i in range(n*2):
            for j in range(n*2):
                for x in range(len(key)):
                    for y in range(len(key[0])):
                        big_lock[i+x][j+y] += key[x][y]
                if check(big_lock):
                    return True
                for x in range(len(key)):
                    for y in range(len(key[0])):
                        big_lock[i+x][j+y] -= key[x][y]
                    
    return answer

def rotate(key):
    n = len(key)
    m = len(key[0])
    new_list = [[0]*n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            new_list[i][j] = key[n-1-j][i]
    return new_list

def check(lock):
    n = len(lock)
    m = len(lock[0])
    length = n//3
    
    for i in range(length, length*2):
        for j in range(length, length*2):
            if lock[i][j] != 1:
                return False
    return True
                
            
    

