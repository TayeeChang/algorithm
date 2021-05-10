# -*- coding: utf-8 -*-
# @Time : 2021/5/10 16:40
# @Author : haojie zhang

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        if fast:  # 奇数
            slow = slow.next

        q = self.traverse(slow)  # 反转后半部分
        p = head
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        return True

    def traverse(self, root):
        p = root
        t = None
        while p:
            q = p.next
            p.next = t
            t = p
            p = q
        return t



