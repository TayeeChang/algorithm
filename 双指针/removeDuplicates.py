# -*- coding: utf-8 -*-
# @Time : 2021/5/7 15:27
# @Author : haojie zhang



from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = fast = 1  # slow 表示新元素要放入的位置
        n = len(nums)
        while fast < n:
            if nums[fast] != nums[slow-1]:  # 区别2: slow-1表示只允许出现一次；slow - n 表示只允许出现 n 次
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow


nums = [1, 1, 1, 1,  2, 3, 4, 4, 4, 4, 5]
s = Solution()
print(s.removeDuplicates(nums))