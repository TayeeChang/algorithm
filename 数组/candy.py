# -*- coding: utf-8 -*-
# @Time : 2021/5/17 15:30
# @Author : haojie zhang

from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)
        res = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1

        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1] + 1)

        return sum(res)

    def candy_with_cycle(self, ratings: List[int]) -> int:

        n = len(ratings)
        minv = float('inf')
        index = 0
        for i in range(n):
            if ratings[i] < minv:
                minv = ratings[i]
                index = i
        new_ratings = ratings[index:] + ratings[:index]
        res = [1] * n
        for i in range(1, n):
            if new_ratings[i] > new_ratings[i-1]:
                res[i] = res[i-1] + 1
        for i in range(n-1, -1, -1):
            if i == n-1:
                if new_ratings[i] > new_ratings[0]:
                    res[i] = max(res[i], res[0]+1)
            elif new_ratings[i] > new_ratings[i+1]:
                res[i] = max(res[i], res[i+1]+1)

        return sum(res)


"""
如果站成一个环，即收尾相连，如何解决？
"""
ratings = [4, 3, 2, 1, 5]
s = Solution()
print(s.candy_with_cycle(ratings))




