# -*- coding: utf-8 -*-
# @Time : 2021/5/12 11:27
# @Author : haojie zhang
"""
1248. 统计「优美子数组」
给你一个整数数组 nums 和一个整数 k。

如果某个 连续 子数组中恰好有 k 个奇数数字，我们就认为这个子数组是「优美子数组」。

请返回这个数组中「优美子数组」的数目。


示例 1：

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。
示例 2：

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。
示例 3：

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16

https://leetcode-cn.com/problems/count-number-of-nice-subarrays/
"""
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        n = len(nums)
        preSum = [0] * (n+1)
        for i in range(n):
            if nums[i] % 2 == 1:
                preSum[i+1] = preSum[i] + 1
            else:
                preSum[i+1] = preSum[i]

        hashMap = defaultdict(int)
        hashMap[0] = 1
        res = 0
        for i in range(len(nums)):
            if preSum[i+1]-k in hashMap:
                res += hashMap[preSum[i+1]-k]
            hashMap[preSum[i+1]] += 1
        return res


nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
s = Solution()
print(s.numberOfSubarrays(nums, k))