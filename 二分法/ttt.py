# -*- coding: utf-8 -*-
# @Time : 2021/4/28 16:51
# @Author : haojie zhang

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(nums1, index1, nums2, index2, k):
            """
            - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
            - 这里的 "/" 表示整除
            - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
            - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
            - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
            - 这样 pivot 本身最大也只能是第 k-1 小的元素
            - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
            - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
            - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
            """
            m = len(nums1)
            n = len(nums2)
            if index1 == m:
                return nums2[index2 + k - 1]
            if index2 == n:
                return nums1[index1 + k - 1]
            if k == 1:
                return min(nums1[index1], nums2[index2])

            newsIndex1 = min(index1 + k//2 -1, m-1)
            newsIndex2 = min(index2 + k//2 -1, n-1)
            pivot1, pivot2 = nums1[newsIndex1], nums2[newsIndex2]
            if pivot1 <= pivot2:
                return getKthElement(nums1, newsIndex1+1, nums2, index2, k - (newsIndex1 - index1 + 1))
            else:
                return getKthElement(nums1, index1, nums2, newsIndex2+1, k - (newsIndex2 - index2 + 1))


        m, n = len(nums1), len(nums2)
        totalLength = m + n
        c = (totalLength + 1) // 2
        if totalLength % 2 == 1:
            return getKthElement(nums1, 0, nums2, 0, c)
        else:
            return (getKthElement(nums1, 0, nums2, 0, c) + getKthElement(nums1, 0, nums2, 0, c+1)) / 2


nums1 = [1]
nums2 = [2, 3, 4, 5, 6]
print(Solution().findMedianSortedArrays(nums1, nums2))