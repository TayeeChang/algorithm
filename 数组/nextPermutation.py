# -*- coding: utf-8 -*-
# @Time : 2021/5/4 15:34
# @Author : haojie zhang

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            m, n = 0, len(nums)-1
            while m < n:
                nums[m], nums[n] = nums[n], nums[m]
                m += 1
                n -= 1
            return
        i -= 1
        # 找到第一个大于A[i]的元素
        j = len(nums) - 1
        while j > i:
            if nums[j] > nums[i]:
                break
            j -= 1
        # 交换
        nums[i], nums[j] = nums[j], nums[i]
        # 逆序变顺序
        m, n = i+1, len(nums)-1
        while m <= n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1

        return


nums = [3, 2, 1]
s = Solution()
print(s.nextPermutation(nums))
