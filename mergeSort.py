# -*- coding: utf-8 -*-
# @Time : 2021/4/21 13:33
# @Author : haojie zhang


def merge(nums, low, mid, high):
    tmp = []
    i, j = low, mid + 1
    while i <= mid and j <= high:
        if nums[i] <= nums[j]:
            tmp.append(nums[i])
            i += 1
        else:
            tmp.append(nums[j])
            j += 1
    tmp += nums[i:mid + 1]
    tmp += nums[j:high + 1]
    nums[low:high + 1] = tmp


def mergeSort(nums, low, high):
    if low >= high:
        return
    mid = low + (high - low) // 2
    mergeSort(nums, low, mid)
    mergeSort(nums, mid + 1, high)
    merge(nums, low, mid, high)


nums = [1, 1, 4, 3, 2, 1, 5, 9, 0]
mergeSort(nums, 0, len(nums) - 1)
print(nums)