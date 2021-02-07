#!/usr/bin/env python
# coding: utf-8

# In[35]:


from collections import deque

N, M, K, X = map(int,input().split())

road = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int,input().split())
    road[s].append(e)


q = deque([X])

dist = [-1] * (N+1)
dist[X] = 0


while q:
    tmp = q.popleft()
    for i in road[tmp]:
        if dist[i] == -1:
            dist[i] = dist[tmp] + 1
            q.append(i)
    

ans = False
    
for idx,i in enumerate(dist):
    if i == K:
        print(idx)
        ans = True

if not ans:
    print(-1)
        

    
    

