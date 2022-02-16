#!/usr/bin/env python
# coding: utf-8

# In[2]:


def longestPalindrome(s: str) -> str:
 
        def check(left: int, right: int, strs: list[str]) -> list[int]:
            while left >= 0 and right <= len(strs) -1 and strs[left] == strs[right]:
                left -= 1
                right += 1
            return strs[left+1 : right]
    
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        ans =''
        for i in range(len(s)):
            ans = max(ans, check(i,i+1,s), check(i,i+2,s),key =len)
            
        return ans

