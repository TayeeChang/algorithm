# -*- coding: utf-8 -*-
# @Time : 2021/6/2 16:24
# @Author : haojie zhang

from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def traverse(root, level, left_to_right):
            if not root:
                return
            if level > len(res):
                res.append([])
            if left_to_right:
                res[level-1].append(root.val)
            if not left_to_right:
                res[level-1].insert(0, root.val)
            traverse(root.left, level+1, not left_to_right)
            traverse(root.right, level + 1, not left_to_right)

        res = []
        traverse(root, 1, True)
        return res