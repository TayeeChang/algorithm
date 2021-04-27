# -*- coding: utf-8 -*-
# @Time : 2021/4/27 10:44
# @Author : haojie zhang

import collections
from typing import List


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

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p != root_q:
            self.pre[root_p] = root_q
            self.cnt -= 1


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        uf = UnionFind(n)
        emailToid = {}
        for i in range(len(accounts)):
            for email in accounts[i][1:]:
                if email not in emailToid:
                    emailToid[email] = i
                else:
                    uf.union(i, emailToid[email])
        id2emial = dict()
        for email, idx in emailToid.items():
            p = uf.find(idx)
            if p not in id2emial:
                id2emial[p] = [email]
            else:
                id2emial[p].append(email)

        res = []
        for idx, emails in id2emial.items():
            name = accounts[idx][0]
            emails.sort()
            res.append([name] + emails)
        return res


accounts = [["Hanzo","Hanzo2@m.co","Hanzo3@m.co"],
            ["Hanzo","Hanzo4@m.co","Hanzo5@m.co"],
            ["Hanzo","Hanzo0@m.co","Hanzo1@m.co"],
            ["Hanzo","Hanzo3@m.co","Hanzo4@m.co"],
            ["Hanzo","Hanzo7@m.co","Hanzo8@m.co"],
            ["Hanzo","Hanzo1@m.co","Hanzo2@m.co"],
            ["Hanzo","Hanzo6@m.co","Hanzo7@m.co"],
            ["Hanzo","Hanzo5@m.co","Hanzo6@m.co"]]

print(Solution().accountsMerge(accounts))



