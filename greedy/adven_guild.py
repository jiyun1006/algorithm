#!/usr/bin/env python
# coding: utf-8

# In[31]:


N = int(input())
tmp = input().split()
ad_list = {}

for num in tmp:
    if num not in ad_list:
        ad_list[num] = 0 
   
    ad_list[num] += 1
    
ad_list = sorted(ad_list.items())

cnt = 0
tmp = 0
for i in ad_list:
    if int(i[0]) == 1:
        cnt += i[1]
        continue
    if int(i[0]) <= i[1]:
        cnt += i[1]//int(i[0])
        tmp += i[1]%int(i[0])
    else:
        if int(i[0]) <= tmp:
            cnt += tmp//int(i[0])
            tmp = tmp%int(i[0])
        else:
            tmp += i[1]
        
print(cnt)


# In[37]:


N = int(input())
ad_list = list(map(int,input().split()))

ad_list.sort()

tmp = 0
cnt = 0

for ad in ad_list:
    tmp += 1
    if 
    

