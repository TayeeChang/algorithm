# -*- coding: utf-8 -*-
# @Time : 2021/5/18 15:06
# @Author : haojie zhang

from 链表 import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        dummy = ListNode(-1)
        dummy.next = head

        p = q = dummy
        # 先走 n 步
        for i in range(n):
            q = q.next
        # 同时走
        while q.next:
            p = p.next
            q = q.next

        p.next = p.next.next

        return dummy.next