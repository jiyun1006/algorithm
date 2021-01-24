#!/usr/bin/env python
# coding: utf-8

# In[3]:


n = 1260
coin_list = [500,100,50,10]

cnt = 0

for coin in coin_list:
    cnt += n//coin
    n %= coin
    
    


# In[13]:


N = 5
M = 8
K = 3

num = [2,4,5,4,6]

tmp = max(num)
num.remove(max(num))


if tmp == max(num):
    ans = tmp * M
else:
    ans = tmp*(M//K)*K + max(num)*(M%K)
    
print(ans)


# In[31]:


N, M = map(int,input().split())

num_list = [list(map(int,input().split())) for x in range(N)]
max = 0

for num in num_list:
    if max < min(num):
        max = min(num)
print(max)


# In[34]:


N, K = map(int, input().split())
cnt = 0

while N > 1:
    if N%K == 0:
        cnt += 1
        N = N//K
    else:
        N -= 1
        cnt += 1
        
print(cnt)

