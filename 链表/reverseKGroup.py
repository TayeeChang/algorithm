# -*- coding: utf-8 -*-
# @Time : 2021/4/24 19:06
# @Author : haojie zhang

#反转以head为头结点的链表
def reverse(head):
    t = None
    p = head
    while p:
        q = p.next
        p.next = t
        t = p
        p = q
    return t


# 反转区间[a, b)之间的元素
def reverse1(a, b):
    t = None
    p = a
    while p != b:
        q = p.next
        p.next = t
        t = p
        p = q
    return t


class Solution:
    def reverse(self, a, b):
        t = None
        p = a
        while p != b:
            q = p.next
            p.next = t
            t = p
            p = q
        return t

    def reverseKGroup(self, head, k: int):
        if not head:
            return None
        a = b = head
        for i in range(k):
            if not b:  # 如果节点总数不是 k 的整数倍，那么将最后剩余的节点保持原有顺序
                return head
            b = b.next
        newHead = self.reverse(a, b)
        head.next = self.reverseKGroup(b, k)
        return newHead








