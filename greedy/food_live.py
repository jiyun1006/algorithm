#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import heapq

def solution(food_times, k):
    answer = 0
    if sum(food_times) <=k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    time_len = len(food_times)
    pre = 0 
    total = 0 
    while total + ((q[0][0]- pre) * time_len) <= k:
        now = heapq.heappop(q)[0]
        total += (now - pre)* time_len
        time_len -= 1
        pre = now
        
        
    
    ans = sorted(q, key = lambda x : x[1])
    
    return ans[(k-total) % time_len][1]
    
    

