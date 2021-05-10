# -*- coding: utf-8 -*-
# @Time : 2021/5/10 14:18
# @Author : haojie zhang


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        n = 1
        p = head
        while p.next:
            p = p.next
            n += 1
        k = k % n
        p.next = head
        newHead = head
        for i in range(n-k):
            pre = newHead
            newHead = newHead.next
        pre.next = None
        return newHead

