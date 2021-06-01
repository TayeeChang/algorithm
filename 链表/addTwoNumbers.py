# -*- coding: utf-8 -*-
# @Time : 2021/5/18 11:08
# @Author : haojie zhang


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p, q = l1, l2
        carry = 0
        dummy = ListNode(-1)
        curr = dummy
        while p or q:
            x1 = p.val if p else 0
            x2 = q.val if q else 0
            val = (x1 + x2 + carry) % 10
            carry = (x1 + x2 + carry) // 10
            curr.next = ListNode(val)
            p = p.next if p else None
            q = q.next if q else None
            curr = curr.next

        if carry:
            curr.next = ListNode(carry)

        return dummy.next