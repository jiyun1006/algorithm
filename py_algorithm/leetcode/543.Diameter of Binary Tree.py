#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    longest = 0
    
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        
        def dfs(node: TreeNode):
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.longest = max(self.longest, (left+right+2))
            
            return max(left, right) + 1
        
        dfs(root)
        return self.longest

