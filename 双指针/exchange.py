# -*- coding: utf-8 -*-
# @Time : 2021/5/10 17:14
# @Author : haojie zhang

from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l] % 2 == 1:
                l += 1
                continue
            if nums[r] % 2 == 0:
                r -= 1
                continue
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        return nums

    def exchange1(self, nums: List[int]) -> List[int]:
        from collections import deque
        queue = deque()
        eventNumber = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                eventNumber += 1
                queue.append(nums[i])
            else:
                nums[i-eventNumber] = nums[i]
        for i in range(len(nums)-eventNumber, len(nums)):
            nums[i] = queue.popleft()
        return nums


nums = [1, 2, 3, 4]
s = Solution()
print(s.exchange1(nums))
