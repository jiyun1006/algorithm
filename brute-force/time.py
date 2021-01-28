#!/usr/bin/env python
# coding: utf-8

# In[5]:


ans = 0
N = int(input())
for i in range(N):
    if i == 3 or i == 13 or i == 23:
        ans += 60*60
    else:
        ans += 15 + 15*60

