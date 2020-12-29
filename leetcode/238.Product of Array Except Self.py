#!/usr/bin/env python
# coding: utf-8

# In[2]:


# O(n)으로 풀이하기 위해서, 나눗셈을 이용하지 않기 위해서는,
# 자기자신을 제외한 왼쪽의 곱과 오른쪽의 곱을 곱하는 방법이 있다.

# 왼쪽 곱 1 1(1) 2(1*2) 6(1*2*3)
# 오른쪽 곱 1 4(4) 12(3*4) 24(2*3*4)


def productExceptSelf(nums: List[int]) -> List[int]:
        a = 1
        temp = []
        for i in nums:
            temp.append(a)
            a*=i
        a = 1
        
        for j in range(len(nums), 0, -1):
            temp[j-1]*=a
            a*=nums[j-1]
        return temp
            
    

