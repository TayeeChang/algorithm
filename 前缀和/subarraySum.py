# -*- coding: utf-8 -*-
# @Time : 2021/4/27 14:28
# @Author : haojie zhang


from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        n = len(nums)
        preSum = [0] * (n+1)
        hashMap = defaultdict(int)
        hashMap[0] = 1
        res = 0
        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]
            res += hashMap[preSum[i+1]-k]
            hashMap[preSum[i + 1]] += 1
        return res


nums = [1]
k = 0
print(Solution().subarraySum(nums, k))
