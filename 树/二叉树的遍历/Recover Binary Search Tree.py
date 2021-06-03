# -*- coding: utf-8 -*-
# @Time : 2021/6/2 18:21
# @Author : haojie zhang

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inOrder(root):
            if not root:
                return []
            return inOrder(root.left) + [(root, root.val)] + inOrder(root.right)

        nums = inOrder(root)
        n1 = 0
        for i in range(len(nums)):
            if i > 0 and nums[i][1] < nums[i-1][1]:
                n1 = i - 1
                break

        n2 = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1 and nums[i][1] > nums[i+1][1]:
                n2 = i + 1
                break

        nums[n1][0].val, nums[n2][0].val = nums[n2][0].val, nums[n1][0].val


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def detect(pre, curr, node):
            if pre and pre.val > curr.val:
                if not node[0]:
                    node[0] = pre
                node[1] = curr

        pre = None
        curr = root
        node = [None, None]
        while curr:
            if curr.left:
                p = curr.left
                while p.right and p.right != curr:
                    p = p.right
                if not p.right:
                    p.right = curr  # 这里不能有pre = curr； 因为pre和curr必须满足顺序关系， 这里curr是pre的左孩子， curr.val < pre.val，不满足顺序关系。
                    curr = curr.left
                    continue
                else:
                    p.right = None
            detect(pre, curr, node)
            pre = curr
            curr = curr.right
        if node[0] and node[1]:
            node[0].val, node[1].val = node[1].val, node[0].val



