#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def invertTree(self, root: TreeNode) -> TreeNode:
        
        queue = collections.deque([root])

        while queue:
        
            node = queue.pop()
            
            if node:
                node.left, node.right = node.right, node.left
            
                queue.append(node.left)
                queue.append(node.right)
                
        return root 
            

