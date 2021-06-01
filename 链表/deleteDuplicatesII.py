# -*- coding: utf-8 -*-
# @Time : 2021/5/18 13:43
# @Author : haojie zhang

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 迭代版
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        p = head

        while p:
            while p.next and p.val == p.next.val:
                p = p.next
            if pre.next == p:
                pre = pre.next
                p = p.next
            else:
                pre.next = p.next
                p = p.next
        return dummy.next


# 递归版
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        if head.val != head.next.val:
            head.next = self.deleteDuplicates(head.next)
            return head
        else:
            while head.next and head.next.val == head.val:
                head = head.next
            return self.deleteDuplicates(head.next)



