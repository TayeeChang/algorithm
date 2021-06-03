# -*- coding: utf-8 -*-
# @Time : 2021/6/3 14:40
# @Author : haojie zhang

# 递归版本


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        if not root.left:
            return

        p = root.left
        while p.right:
            p = p.right

        p.right = root.right
        root.right = root.left
        root.left = None


#  迭代版本
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
        stack = [root]
        pre = None
        while stack:
            node = stack.pop()
            if pre:
                pre.right = node
                pre.left = None

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            pre = node







