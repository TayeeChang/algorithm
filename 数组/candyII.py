# -*- coding: utf-8 -*-
# @Time : 2021/5/17 15:50
# @Author : haojie zhang


from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:

        ratings = [ratings[-1]] + ratings + [ratings[0]]

        n = len(ratings)
        res = [1] * n
        for i in range(1, n-1):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1



        return 0