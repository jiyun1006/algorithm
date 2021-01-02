#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        dic = collections.defaultdict(list)
        dist = collections.defaultdict(int)
        
        for i, j, k in flights:
            dic[i].append([j,k])
            
        q = [(0, src, K)]
            
        while q:
            p, node, k = heapq.heappop(q)
            
            if node == dst:
                return p
            if k >= 0:
                for a, b in dic[node]:
                    t = p + b
                    heapq.heappush(q, (t, a, k-1))

