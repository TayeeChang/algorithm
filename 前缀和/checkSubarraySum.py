# -*- coding: utf-8 -*-
# @Time : 2021/5/12 14:43
# @Author : haojie zhang

from typing import List

"""
关键在于判断子数组的长度 >= 2
"""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict
        n = len(nums)
        preSum = [0] * (n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]
        hashMap = defaultdict(int)
        hashMap[0] = -1
        for i in range(n):
            m = preSum[i+1] % k
            if m in hashMap:
                if i - hashMap[m] >= 2:
                    return True
                continue
            hashMap[m] = i
        return False


nums = [23, 2, 4, 6, 6]
k = 7
s = Solution()
print(s.checkSubarraySum(nums, k))
