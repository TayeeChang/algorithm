# -*- coding: utf-8 -*-
# @Time : 2021/4/29 16:55
# @Author : haojie zhang


from typing import List

# 解法一  递归加记忆化搜索
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def traceback(nums, target):
            if target == 0:
                return 1
            if target < 0:
                return 0
            if target in hashMap:
                return hashMap[target]
            res = 0
            for num in nums:
                res += traceback(nums, target-num)
            hashMap[target] = res
            return res

        hashMap = {}
        traceback(nums, target)

        return hashMap[target]


    def combinationSum4_dp(self, nums: List[int], target: int) -> int:
        dp = [0] * (target+1)
        dp[0] = 1
        for i in range(1, target+1):
            for j in nums:
                if i >= j:
                    dp[i] += dp[i-j]
        return dp[-1]


nums = [1, 3]
target = 4
s = Solution()
print(s.combinationSum4_dp(nums, target))










