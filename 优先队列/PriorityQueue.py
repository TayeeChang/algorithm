# -*- coding: utf-8 -*-
# @Time : 2021/4/24 12:57
# @Author : haojie zhang


class PriorityQueue:
    def __init__(self, heap=[]):
        self.heap = heap

    def min_heapify(self, start, end):
        """ 最小堆化：使以start为根的子树成为最小堆. """
        left = 2 * start + 1
        right = 2 * start + 2
        smallest_index = start
        if left <= end and self.heap[smallest_index] > self.heap[left]:
            smallest_index = left
        if right <= end and self.heap[smallest_index] > self.heap[right]:
            smallest_index = right
        if smallest_index != start:
            self.heap[start], self.heap[smallest_index] = self.heap[smallest_index], self.heap[start]
            self.min_heapify(smallest_index, end)

    def insert(self, val):
        """ 插入元素需要上浮 """
        self.heap.append(val)
        idx = len(self.heap) - 1
        parIdx = (idx - 1) // 2
        while parIdx >= 0:
            if self.heap[parIdx] > self.heap[idx]:
                self.heap[parIdx], self.heap[idx] = self.heap[idx], self.heap[parIdx]
                parIdx = (idx - 1) // 2
            else:
                break

    def delete(self):
        """ 删除元素需要下沉 """
        last = len(self.heap) - 1
        if last < 0:
            return None
        self.heap[0], self.heap[last] = self.heap[last], self.heap[0]
        val = self.heap.pop()
        self.min_heapify(0, len(self.heap)-1)
        return val

    def build_min_heapify(self):
        """ 建立最小堆, O(nlog(n)) """
        n = len(self.heap)
        for i in range(n//2-1, -1, -1):
            self.min_heapify(i, n-1)

    def show(self):
        print(self.heap)


nums = [1, 3, 2, 4, 8, 6, 22, 9]
pq = PriorityQueue()
n = len(nums)
for num in nums:
    pq.insert(num)
    pq.show()

for i in range(n):
    pq.delete()
    pq.show()
