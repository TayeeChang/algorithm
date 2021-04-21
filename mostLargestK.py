# -*- coding: utf-8 -*-
# @Time : 2021/4/21 16:00
# @Author : haojie zhang


def build_heap(nums, start, end):
    left = 2 * start + 1
    right = 2 * start + 2
    least_index = start
    if left <= end and nums[least_index] > nums[left]:
        least_index = left
    if right <= end and nums[least_index] > nums[right]:
        least_index = right
    # 通过上面跟左右节点比较后，得出三个元素之间较大的下标，如果较大下标不是父节点的下标，说明交换后需要重新调整大顶堆
    if least_index != start:
        nums[least_index], nums[start] = nums[start], nums[least_index]
        build_heap(nums, least_index, end)


def findKLargest(nums, k):
    if len(nums) <= k:
        return nums
    n = len(nums)
    tmp = nums[:k]
    for i in range(k//2-1, -1, -1):
        build_heap(tmp, i, k-1)
    for i in range(k, n):
        if nums[i] > tmp[0]:
            tmp[0] = nums[i]
            build_heap(tmp, 0, k-1)
    return tmp


nums = [1, 7, 2, 8, 3, 9, 4, 10]
res = findKLargest(nums, 5)
print(res)




