# -*- coding: utf-8 -*-
# @Time : 2021/4/26 16:46
# @Author : haojie zhang

from typing import List


# 右插位置对应的数一定是右边第一个大于目标数的数
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        low, high = 0, len(letters)
        while low < high:
            mid = low + (high - low) // 2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid
        return letters[low % len(letters)]   #


letters = ["c", "f", "j"]
target = "j"
print(Solution().nextGreatestLetter(letters, target))