# -*- coding: utf-8 -*-
# @Time : 2021/6/2 16:03
# @Author : haojie zhang
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            next_level = []
            curr = []
            for node in stack:
                curr.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            stack = next_level
            res.append(curr)

        return res


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        def traverse(root, level):
            if not root:
                return
            if level > len(res):
                res.append([])

            res[level-1].append(root.val)
            traverse(root.left, level+1)
            traverse(root.right, level+1)

        res = []
        traverse(root, 1)
        return res
