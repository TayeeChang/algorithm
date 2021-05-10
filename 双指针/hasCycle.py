# -*- coding: utf-8 -*-
# @Time : 2021/5/10 16:07
# @Author : haojie zhang

"""
判断链表是否存在环。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

