# -*- coding: utf-8 -*-
# @Time : 2021/4/27 9:35
# @Author : haojie zhang


class UnionFind:
    def __init__(self, n):
        self.pre = [i for i in range(n)]
        self.cnt = n

    def find(self, x):
        root = x
        while self.pre[root] != root:
            root = self.pre[root]

        # 路径压缩
        while x != root:
            parent = self.pre[x]
            self.pre[x] = root
            x = parent

        return root

    def join(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p != root_q:
            self.pre[root_p] = root_q
            self.cnt -= 1


from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j]:
                    uf.join(i, j)
        return uf.cnt








