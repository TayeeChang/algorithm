# -*- coding: utf-8 -*-
# @Time : 2021/4/21 15:32
# @Author : haojie zhang


class Solution:
    def heap_sort(self, nums):
        n = len(nums)
        # 构造大顶堆，从非叶子节点开始倒序遍历，因此是n//2 -1 就是最后一个非叶子节点
        for i in range(n//2-1, -1, -1):
            self.build_heap(nums, i, n-1)
        # 上面的循环完成了大顶堆的构造，那么就开始把根节点跟末尾节点交换，然后重新调整大顶堆
        for j in range(n-1, 0, -1):
            nums[0], nums[j] = nums[j], nums[0]
            self.build_heap(nums, 0, j-1)

        return nums

    def build_heap(self, nums, start, end):
        left = 2 * start + 1
        right = 2 * start + 2
        large_index = start
        if left <= end and nums[large_index] < nums[left]:
            large_index = left
        if right <= end and nums[large_index] < nums[right]:
            large_index = right
        # 通过上面跟左右节点比较后，得出三个元素之间较大的下标，如果较大下标不是父节点的下标，说明交换后需要重新调整大顶堆
        if large_index != start:
            nums[large_index], nums[start] = nums[start], nums[large_index]
            self.build_heap(nums, large_index, end)


nums = [1, 2, 4, 3, 5, 0]
s = Solution()
nums_sort = s.heap_sort(nums)
print(nums_sort)
