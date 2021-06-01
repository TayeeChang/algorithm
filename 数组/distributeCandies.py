# -*- coding: utf-8 -*-
# @Time : 2021/5/17 15:00
# @Author : haojie zhang

from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        sums = len(candyType) // 2
        kinds = len(set(candyType))

        return min(sums, kinds)


candyType = [1,1,2,3]
