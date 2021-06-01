# -*- coding: utf-8 -*-
# @Time : 2021/5/18 14:35
# @Author : haojie zhang

from 链表 import ListNode

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        # 计算链表长度
        cnt = 1
        p = head
        while p.next:
            cnt += 1
            p = p.next

        k = cnt - k % cnt
        p.next = head  # 首尾相连

        for i in range(k):
            p = p.next

        newHead = p.next  # 新的首节点
        p.next = None  # 断开环
        return newHead





