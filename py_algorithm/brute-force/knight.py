#!/usr/bin/env python
# coding: utf-8

# In[22]:


tmp = input()

loc = [int(tmp[1]), ord(tmp[0])]
start = [1, ord("a")]
end = [8, ord("h")]
print(loc)
ans = 0

if loc[0]-2 >= start[0]:
    if loc[1]-1 >= start[1]:
        ans += 1
    if loc[1]+1 <= end[1]:
        ans += 1
        

if loc[0] +2 <= end[0]:
    if loc[1] -1 >= start[1]:
        ans += 1
    if loc[1]+1 <= end[1]:
        ans+=1

if loc[1] -2 >= start[1]:
    if loc[0] -1 >= start[0]:
        ans += 1
    if loc[0] +1 <= end[0]:
        ans += 1

if loc[1] +2 <= end[1]:
    if loc[0] -1 >= start[0]:
        ans += 1
    if loc[0] +1 <= end[0]:
        ans += 1

print(ans)
    

