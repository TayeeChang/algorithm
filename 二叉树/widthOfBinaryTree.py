# -*- coding: utf-8 -*-
# @Time : 2021/4/30 9:53
# @Author : haojie zhang


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [[root, 0]]
        res = 0
        while stack:
            n = len(stack)
            next_layer = []
            left = float('inf')
            right = 0
            for i in range(n):
                node, pos = stack[i]
                left = min(left, pos)
                right = max(right, pos)
                if node.left:
                    next_layer.append([node.left, pos*2])
                if node.right:
                    next_layer.append([node.right, pos*2+1])
            res = max(res, right-left+1)
            stack = next_layer
        return res





