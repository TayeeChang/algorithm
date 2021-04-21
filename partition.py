# -*- coding: utf-8 -*-
# @Time : 2021/4/21 16:17
# @Author : haojie zhang


def partition(nums, left, right):
    if left >= right:
        return left
    low, high = left, right
    while left < right:
        while left < right and nums[right] >= nums[low]:
            right -= 1
        while left < right and nums[left] <= nums[low]:
            left += 1
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    nums[low], nums[left] = nums[left], nums[low]
    return left


def findKLargest(nums, k):
    n = len(nums)
    if n <= k:
        return nums
    k = n - k
    low, high = 0, n-1
    while low <= high:
        p = partition(nums, low, high)
        if p > k:
            high = p - 1
        elif p < k:
            low = p + 1
        elif p == k:
            break
    return nums[k:]


nums = [1, 7, 2, 8, 3, 9, 4, 10]
res = findKLargest(nums, 5)
print(res)