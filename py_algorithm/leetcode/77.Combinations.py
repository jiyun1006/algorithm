#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def combine(n: int, k: int) -> List[List[int]]:
       
       if n <= 1:
           return [[n]]
               
       def DFS(strs, idx):
           
           if not strs:
               strs.append(idx)
           
           if len(strs) == k:
               ans.append(strs)
               return 
       
           for i in range(idx, n+1):
               if i in strs:
                   continue
               temp = strs[:]
               temp.append(i)
               DFS(temp, i)

       
       ans = []
       
       for i in range(1, n+1):
           strs = []
           DFS(strs, i)
           
       return ans

