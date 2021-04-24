# -*- coding: utf-8 -*-
# @Time : 2021/4/24 15:19
# @Author : haojie zhang

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        window = deque()
        res = []
        for i in range(len(nums)):
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            while window and i - window[0] == k:
                window.popleft()
            window.append(i)
            if i >= k-1:
                res.append(nums[window[0]])

        return res


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
s = Solution()
print(s.maxSlidingWindow(nums, k))