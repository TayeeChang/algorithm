# -*- coding: utf-8 -*-
# @Time : 2021/4/30 9:35
# @Author : haojie zhang

from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def traceback(nums, k, bucket, start, used, target):
            if k == 0:
                return True
            if bucket == target:
                return traceback(nums, k-1, 0, 0, used, target)

            for i in range(start, len(nums)):
                if used[i]:
                    continue
                if bucket + nums[i] > target:
                    break
                used[i] = True
                if traceback(nums, k, bucket+nums[i], i+1, used, target):
                    return True
                used[i] = False

            return False

        if len(nums) < k:
            return False
        if sum(nums) % k:
            return False
        target = sum(nums) // k
        nums.sort()
        used = [False] * len(nums)
        return traceback(nums, k, 0, 0, used, target)

