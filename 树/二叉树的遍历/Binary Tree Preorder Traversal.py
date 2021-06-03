# -*- coding: utf-8 -*-
# @Time : 2021/6/2 17:09
# @Author : haojie zhang

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 前序遍历
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# 使用栈
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

# Morris遍历
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        curr = root
        while curr:
            mostRight = curr.left
            if mostRight:
                while mostRight.right and mostRight.right != curr:
                    mostRight = mostRight.right
                if not mostRight.right:
                    res.append(curr.val)
                    mostRight.right = curr
                    curr = curr.left
                    continue
                else:
                    mostRight.right = None
            else:
                res.append(curr.val)
            curr = curr.right
        return res







