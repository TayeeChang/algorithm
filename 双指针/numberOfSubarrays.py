# -*- coding: utf-8 -*-
# @Time : 2021/5/12 10:21
# @Author : haojie zhang

from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        left = right = 0
        l = r = 0
        while right < len(nums):
            if nums[right] % 2 == 1:
                k -= 1
            right += 1
            if k == 0:
                l = r = 0

            while k < 0:
                if nums[left] % 2 == 1:
                    k += 1
                left += 1
                l += 1

        return res


nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
k = 2
s = Solution()
print(s.numberOfSubarrays(nums, k))
