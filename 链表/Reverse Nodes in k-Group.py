# -*- coding: utf-8 -*-
# @Time : 2021/5/18 15:48
# @Author : haojie zhang


from 链表 import ListNode

# 递归版


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:

        if not head:
            return head

        i = 0
        p = head
        while i < k:
            if not p:
                break
            p = p.next
            i += 1
        if i < k:
            return head

        newHead = self.reverse(head, k)
        head.next  = self.reverseKGroup(p, k)
        return newHead

    def reverse(self, head, k):
        p = head
        t = None
        for i in range(k):
            if not p:
                break
            q = p.next
            p.next = t
            t = p
            p = q
        return t
