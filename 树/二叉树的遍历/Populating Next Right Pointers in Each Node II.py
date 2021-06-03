# -*- coding: utf-8 -*-
# @Time : 2021/6/3 15:21
# @Author : haojie zhang

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        curr = root
        while curr:
            dummy = Node(0)
            pre = dummy
            while curr:
                if curr.left:
                    pre.next = curr.left
                    pre = pre.next
                if curr.right:
                    pre.next = curr.right
                    pre = pre.next
                curr = curr.next

            curr = dummy.next
        return root



