#!/usr/bin/env python
# coding: utf-8

# In[8]:


def subsets(nums: List[int]) -> List[List[int]]:
        
        
        def DFS(ans: List, idx: int):
            result.append(ans)
            
            for i in range(idx, len(nums)):
                
                DFS(ans + [nums[i]], i+1)
                
        result = []
        ans = []
        index = 0
            
        DFS(ans, index)
        return result

