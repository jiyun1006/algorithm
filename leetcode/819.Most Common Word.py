#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 정규표현식과 Couter 메소드로 푼 코드. --> 제일 빠름.

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^\w]',' ',paragraph)

        a = paragraph.split()
        a_dict = dict()
        for i in a:
            if i in banned:
                continue
            if i not in a_dict:
                a_dict[i] = 0
            a_dict[i] += 1
        b = collections.Counter(a_dict)
        
        return b.most_common(1)[0][0]


# In[ ]:


# 딕셔너리 생성없이 바로 리스트 활용.

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        paragraph = re.sub('[^\w]',' ',paragraph)
        a = paragraph.split()
        b = list()
        for i in a:
            if i in banned:
                continue
            else:
                b.append(i)
        c = collections.Counter(b)
        
        return c.most_common(1)[0][0]


# In[ ]:


# 리스트 컴프리헨션문법으로 코드길이 축소.

def mostCommonWord(paragraph: str, banned: List[str]) -> str:
        a = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
        
        b = collections.Counter(a)
        
        return b.most_common(1)[0][0]
        

