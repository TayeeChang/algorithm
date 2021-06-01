# -*- coding: utf-8 -*-
# @Time : 2021/5/18 15:18
# @Author : haojie zhang

from 链表 import ListNode

# 递归版


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        p = head.next.next
        newHead = head.next
        newHead.next = head
        head.next = self.swapPairs(p)
        return newHead


# 迭代版

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        p = head
        while p and p.next:
            q = p.next.next
            pre.next = p.next
            p.next.next = p
            p.next = q
            pre = p
            p = q

        return dummy.next


