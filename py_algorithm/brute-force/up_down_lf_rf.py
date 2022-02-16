#!/usr/bin/env python
# coding: utf-8

# In[5]:


N = int(input())

drt = input().split()

loc = [1,1]


for tmp in drt:
    if tmp == "R":
        if loc[1] == N:
            continue
        loc[1] += 1
    
    elif tmp == "L":
        if loc[1] == 1:
            continue
        loc[1] -= 1
        
    elif tmp == "D":
        if loc[0] == N:
            continue
        loc[0] += 1
        
    elif tmp == "U":
        if loc[0] == 1:
            continue
        loc[0] -= 1
print(loc)
    

