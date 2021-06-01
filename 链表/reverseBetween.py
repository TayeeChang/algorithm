# -*- coding: utf-8 -*-
# @Time : 2021/5/13 10:20
# @Author : haojie zhang

# 头插法


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = p = dummy

        for i in range(left):
            pre = p
            p = p.next

        for i in range(right-left):
            q = p.next
            p.next = q.next
            q.next = pre.next
            pre.next = q

        return dummy.next