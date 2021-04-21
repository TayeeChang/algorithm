# -*- coding: utf-8 -*-
# @Time : 2021/4/21 11:10
# @Author : haojie zhang

# 快排


def quickSort(nums, left, right):
    if left >= right:
        return
    low, high = left, right
    while left < right:
        while left < right and nums[right] >= nums[low]:
            right -= 1
        while left < right and nums[left] <= nums[low]:
            left += 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]

    nums[low], nums[left] = nums[left], nums[low]

    quickSort(nums, left + 1, high)
    quickSort(nums, low, left - 1)


nums = [2, 3, 1, 1, 4]
quickSort(nums, 0, len(nums) - 1)
print(nums)
