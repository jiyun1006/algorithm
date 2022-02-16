#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    ans = len(dist) + 1
    for i in range(length):
        for person in list(permutations(dist, len(dist))):
            cnt = 1
            loc = weak[i] + person[cnt - 1]
            for idx in range(i, i+length):
                if loc < weak[idx]:
                    cnt += 1
                    if cnt > len(dist):
                        break
            
                    loc = weak[idx] + person[cnt-1]
            ans = min(ans, cnt)
    if ans > len(dist):
        return -1
    return ans            
    

