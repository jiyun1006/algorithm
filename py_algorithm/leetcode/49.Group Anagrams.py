#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# defaultdict를 이용해서 키의 존재 여부 체크를 건너뛸 수 있다.
# 그 다음 같은 문자를 가진 키를 기준으로 리스트를 만들어 ana 리스트에 넣는다.

def groupAnagrams(strs: List[str]) -> List[List[str]]:
        ana = collections.defaultdict(list)
        
        for word in strs:
            ana[''.join(sorted(word))].append(word)
        return ana.values()
        

