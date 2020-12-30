#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 단순 연결 리스트 class.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def isPalindrome(head: ListNode) -> bool:
        temp_list: List = []
        
        if not head:
            return True
        
        node = head
        
        while node is not None:
            temp_list.append(node.val)
            node = node.next
        
        while len(temp_list) > 1:
            if temp_list.pop() != temp_list.pop(0):
                return False
        return True


# In[ ]:


# 리스트 말고 deque를 이용해서 pop(n) 에서 O(n)만큼 걸리는 것을 O(1)으로 줄였다.

def isPalindrome(self, head: ListNode) -> bool:
        
        temp_list: Deque = deque()
        
        if not head:
            return True
        
        node = head
        
        while node is not None:
            temp_list.append(node.val)
            node = node.next
        
        while len(temp_list) > 1:
            if temp_list.pop() != temp_list.popleft():
                return False
        return True

