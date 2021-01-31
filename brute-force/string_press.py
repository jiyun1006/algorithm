#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(s):
    answer = len(s)
    length = len(s)//2
    cnt_list = list()
    for j in range(1,length+1):
        idx, cnt = 0, 1
        tmp = s[0:j]
        tmp2 = ''
        for i in range(j, len(s), j):
            if tmp == s[i:i+j]:
                cnt += 1
            else:
                tmp2 += str(cnt) + tmp if cnt >= 2 else tmp
                tmp = s[i:i+j]
                cnt = 1
            
        tmp2 += str(cnt) + tmp if cnt >= 2 else tmp   
        answer = min(answer, len(tmp2))
    return answer

