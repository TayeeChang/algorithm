# -*- coding: utf-8 -*-
# @Time : 2021/5/10 15:05
# @Author : haojie zhang


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode(-1)
        large = ListNode(-1)
        smallHead = small
        largeHead = large

        p = head
        while p:
            if p.val < x:
                small.next = p
                small = small.next
            else:
                large.next = p
                large = large.next
            p = p.next
        large.next = None
        small.next = largeHead.next
        return smallHead.next


