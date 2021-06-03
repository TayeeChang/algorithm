# -*- coding: utf-8 -*-
# @Time : 2021/6/2 17:30
# @Author : haojie zhang

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Morris遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
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
                    mostRight.right = curr
                    curr = curr.left
                    continue
                else:
                    mostRight.right = None
                    curr = curr.right
            else:
                res.append(curr.val)
                curr = curr.right
        return res


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        res = []
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            node = stack.pop()
            res.append(node.val)

            if node.right:
                root = node.right
        return res
