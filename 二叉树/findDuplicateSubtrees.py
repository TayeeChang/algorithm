# -*- coding: utf-8 -*-
# @Time : 2021/4/30 11:34
# @Author : haojie zhang

from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        from collections import defaultdict
        def helper(root):
            if not root:
                return '#'
            left = helper(root.left)
            right = helper(root.right)
            subTree = left + ',' + right + ',' + str(root.val)
            hashMap[subTree] += 1
            if hashMap[subTree] == 2:
                res.add(root)
            return subTree
        res = set()
        hashMap = defaultdict(int)
        helper(root)
        return list(res)
