# -*- coding: utf-8 -*-
# @Time : 2021/6/3 15:04
# @Author : haojie zhang

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def populate(p, q):
            if not p or not q:
                return

            p.next = q
            populate(p.left, p.right)
            populate(q.left, q.right)
            populate(p.right, q.left)

        if not root:
            return root

        populate(root.left, root.right)
        return root