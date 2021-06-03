# -*- coding: utf-8 -*-
# @Time : 2021/6/3 10:08
# @Author : haojie zhang

# 递归版


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# 迭代版


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        stack = [p, q]
        while stack:
            q = stack.pop()
            p = stack.pop()
            if not p and not q:
                continue
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            stack.append(p.left)
            stack.append(q.left)
            stack.append(p.right)
            stack.append(q.right)
        return True


