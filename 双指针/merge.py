# -*- coding: utf-8 -*-
# @Time : 2021/5/10 15:21
# @Author : haojie zhang

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> List:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i, j = m-1, n-1
        p = m+n-1
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                p -= 1
                i -= 1
            else:
                nums1[p] = nums2[j]
                p -= 1
                j -= 1
        if i == -1:
            nums1[:p+1] = nums2[:j+1]
        return nums1


nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
s = Solution()
print(s.merge(nums1, 3, nums2, 3))
