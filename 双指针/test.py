# -*- coding: utf-8 -*-
# @Time : 2021/5/11 13:54
# @Author : haojie zhang

from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        res = 0
        # 先确定山顶（当前元素比两边大），然后向两边延伸
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]: # 当前左边界，山顶，右边界的下标
                left, top, right = i-1, i, i+1
                while left > 0 and arr[left-1] < arr[left]:
                    left -= 1
                while right < len(arr) - 1 and arr[right+1] < arr[right]:
                    right += 1
                res = max(res, right - left +1)
        return res

