# -*- coding: utf-8 -*-
# @Time : 2021/4/27 14:28
# @Author : haojie zhang

"""
560. 和为K的子数组
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
说明 :

数组的长度为 [1, 20,000]。
数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
https://leetcode-cn.com/problems/subarray-sum-equals-k/
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        n = len(nums)
        preSum = [0] * (n+1)
        for i in range(n):   # 构建前缀和数组
            preSum[i+1] = preSum[i] + nums[i]
        res = 0
        hashMap = defaultdict(int)  # 存储每个（前缀和， 前缀和出现次数）
        hashMap[0] = 1  # 需要预留前缀和为0的情况
        for i in range(n):
            if preSum[i+1] - k in hashMap:
                res += hashMap[preSum[i+1]-k]
            hashMap[preSum[i+1]] += 1

        return res


nums = [1]
k = 0
print(Solution().subarraySum(nums, k))
