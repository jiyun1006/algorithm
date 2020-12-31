#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 중첩함수로 깔끔하게.

def numIslands(grid: List[List[str]]) -> int:   
        def DFS(i: int, j: int):
            if i < 0 or i >= len(grid) or             j < 0 or j >= len(grid[0]) or             grid[i][j] != '1':
                return

            grid[i][j] = '0'

            DFS(i+1, j)
            DFS(i, j+1)
            DFS(i-1, j)
            DFS(i, j-1)
        
        if not grid:
            return 0
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    DFS(i, j)
                    ans += 1
        return ans
                

