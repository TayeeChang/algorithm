# -*- coding: utf-8 -*-
# @Time : 2021/5/10 17:53
# @Author : haojie zhang

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                slow = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow
    """
    # 抽屉原理， 每个数作为下标都与另外一个数唯一对应， 当出现重复的时候，其中一个数会被对应2次，对应2次的数就是重复的数。
    比如：
    [1,3,4,2,3]
    1-> [1, -3, 4, 2, 3]
    3-> [1, -3, 4, -2, 3]
    4-> [1, -3, 4, -2, -3]
    2-> [1, -3, -4, -2, -3]
    3-> 出现重复对应-2，则3就是重复的数。
    
    """
    def findDuplicate1(self, nums: List[int]) -> int:
        for num in nums:
            if nums[abs(num)] > 0:
                nums[abs(num)] *= -1
            else:
                return -num


nums = [1, 3, 4, 2, 2]
s = Solution()
print(s.findDuplicate1(nums))

