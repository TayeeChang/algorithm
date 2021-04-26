# -*- coding: utf-8 -*-
# @Time : 2021/4/26 14:30
# @Author : haojie zhang

"""
将 x 插入排序数组, 并维持排序；
如果 x 已经在数组中，则有两种插入方式：从 x 的最左边插入（左插）、从 x 的最右边插入（右插）

详情可以参考 bisect.
"""


# 右插
def insort_right(nums, target):
    low, high = 0, len(nums)
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


# 左插
def insort_left(nums, target):
    low, high = 0, len(nums)
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


nums = [1, 2, 4, 7]
target = 4
print(insort_right(nums, target))  # 右插位置
print(insort_left(nums, target))   # 左插位置




