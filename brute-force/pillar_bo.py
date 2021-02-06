#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(n, build_frame):
    answer = []
    
    
    for frame in build_frame:
        x, y, pil, inst = frame
        if inst == 0:
            answer.remove([x,y, pil])
            if not check(answer):
                answer.append([x,y,pil])     
        if inst == 1:
            answer.append([x,y,pil])
            if not check(answer):
                answer.remove([x,y,pil])               
            
                  
    return sorted(answer)


def check(answer):
    for x, y, pil in answer:
        if pil == 0:
            if y == 0 or [x, y-1, 0] in answer or [x-1, y, 1] in answer or [x,y,1] in answer:
                continue
            return False
            
        elif pil == 1:
            if [x, y-1, 0] in answer or ([x-1, y, 1] in answer and [x+1, y, 1]) in answer or             [x+1, y-1, 0] in answer:
                continue
            return False
    return True
    

