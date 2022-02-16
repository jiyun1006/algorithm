#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
        
        ans = 0
        ans_list = []
        strs = []
        
        def DFS(ans: int, strs: List):
            if ans > target:
                return 
            
            if ans == target:
                strs = sorted(strs)
                if strs in ans_list:
                    return
                ans_list.append(strs)
                
            
            for i in range(len(candidates)):
                temp  = strs[:]
                temp.append(candidates[i])
                DFS(ans + candidates[i], temp)
        
        DFS(ans, strs)
        return ans_list

