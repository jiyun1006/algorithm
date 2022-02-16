#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def findItinerary(tickets: List[List[str]]) -> List[str]:
               
        dic = collections.defaultdict(list)
        for a,b in sorted(tickets):
            dic[a].append(b)
        
        ans = []
        
        def DFS(strs: str):
            while dic[strs]:
                DFS(dic[strs].pop(0))
            ans.append(strs)
            
        DFS('JFK')
        return ans[::-1]

