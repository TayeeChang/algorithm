# -*- coding: utf-8 -*-
# @Time : 2021/6/3 11:07
# @Author : haojie zhang


"""
* Returns the height of `root` if `root` is a balanced tree,
* otherwise, returns `-1`.
"""

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def balanceHeight(root):
            if not root:
                return 0
            left = balanceHeight(root.left)
            right = balanceHeight(root.right)

            if left < 0 or right < 0 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return balanceHeight(root) >= 0

