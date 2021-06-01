# -*- coding: utf-8 -*-
# @Time : 2021/5/15 22:05
# @Author : haojie zhang

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        from collections import defaultdict
        hashMap = defaultdict(int)
        res = 0
        for num in nums:
            if not hashMap[num]:
                left, right = hashMap[num-1], hashMap[num+1]
                hashMap[num] = left + right + 1
                hashMap[num-left] = hashMap[num]
                hashMap[num+right] = hashMap[num]
                res = max(res, hashMap[num])
        return res


nums = [100,4,200,1,3,2]
s = Solution()
print(s.longestConsecutive(nums))