#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# nested fn
# DFS로 한차례 돈 다음에, 백트래킹으로 결과물을 조합한다.  


def letterCombinations(self, digits: str) -> List[str]:
        
        di_dic = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", 
                 "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        if not digits:
            return []
        ans = []
        def DFS(index, path):
# 첫번째 인자가 아닌 두번째 인자는 여기서 걸러지게 된다.
# path의 길이가 digits의 길이보다 짧지만, index가 digits의 길이와 같아서 밑의 반복문을 실행하지 못한다.
            if len(path) == len(digits):
                ans.append(path)
                return 
        
        
            for i in range(index, len(digits)):
                for j in di_dic[digits[i]]:
                    DFS(i + 1, path + j)

        
        DFS(0, "")
        return ans

