#!/usr/bin/env python
# coding: utf-8

# In[1]:


# deque를 이용해서 pop(0)의 O(n)을 O(1)로 바꿔 실행시간을 줄인 방법

def isPalindrome(self, s: str) -> bool:
        a = deque()
        for char in s:
            if char.isalnum():
                a.append(char.lower())
        while len(a) > 1:
            if a.pop() != a.popleft():
                return False
        return True
    


# In[ ]:


# 정규표현식을 이용해서 문자를 필터링.

def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        
        s = re.sub('[^a-z0-9]', '', s)
        
        return s == s[::-1]
        
        

