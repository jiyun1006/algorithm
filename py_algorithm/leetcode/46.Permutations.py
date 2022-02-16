#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def permute(nums: List[int]) -> List[List[int]]:
        def DFS(strs: List, cnt: int):    
            
            if strs and (len(strs) == len(nums)):
                ans.append(strs)
                return 
            
            if not strs:
                strs.append(nums[cnt])
                
               
            
            for j in nums:

                if j in strs:
                    continue
                temp = strs[:]
                temp.append(j)

                DFS(temp, cnt)

        
        if len(nums) == 1:
            return [nums]
        
        ans = []
        
        for i in range(len(nums)):
            strs = []
            
            DFS(strs, i)
        return ans

