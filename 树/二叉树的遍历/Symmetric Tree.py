# -*- coding: utf-8 -*-
# @Time : 2021/6/3 10:59
# @Author : haojie zhang


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def traverse(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and traverse(p.left, q.right) and traverse(p.right, q.left)
        return traverse(root.left, root.right)


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        stack = [root.left, root.right]
        while stack:
            p, q = stack.pop(), stack.pop()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False

            stack.append(p.left)
            stack.append(q.right)

            stack.append(p.right)
            stack.append(q.left)
        return True