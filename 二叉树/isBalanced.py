# -*- coding: utf-8 -*-
# @Time : 2021/4/30 10:43
# @Author : haojie zhang


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced1(self, root: TreeNode) -> bool:
        """ 自顶向下 """
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def isBalanced2(self, root: TreeNode) -> bool:
        """ 自底向上 """
        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)

            if left != -1 and right != -1 and abs(left-right) <= 1:
                return max(left, right) + 1

            return -1

        return height(root) >= 0


