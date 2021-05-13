# -*- coding: utf-8 -*-
# @Time : 2021/5/13 9:58
# @Author : haojie zhang

"""
930. 和相同的二元子数组
在由若干 0 和 1  组成的数组 A 中，有多少个和为 S 的非空子数组。

示例：

输入：A = [1,0,1,0,1], S = 2
输出：4
解释：
如下面黑体所示，有 4 个满足题目要求的子数组：
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]
[1,0,1,0,1]

https://leetcode-cn.com/problems/binary-subarrays-with-sum/
"""

from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        from collections import defaultdict
        n = len(nums)
        preSum = [0] * (n+1)
        for i in range(n):
            preSum[i+1] = preSum[i] + nums[i]
        res = 0
        hashMap = defaultdict(int)
        hashMap[0] = 1  # 细节1
        for i in range(n):
            if preSum[i+1] - goal in hashMap:
                res += hashMap[preSum[i+1]-goal]
            hashMap[preSum[i+1]] += 1
        return res


A = [1, 0, 1, 0, 1]
S = 2
s = Solution()
print(s.numSubarraysWithSum(A, S))