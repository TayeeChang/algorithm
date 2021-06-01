# -*- coding: utf-8 -*-
# @Time : 2021/5/17 14:48
# @Author : haojie zhang

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sums = 0
        total = 0
        j = 0
        for i in range(len(gas)):
            sums += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if sums < 0:
                sums = 0
                j = i+1
        if total >= 0:
            return j
        return -1


gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
s = Solution()
print(s.canCompleteCircuit(gas, cost))