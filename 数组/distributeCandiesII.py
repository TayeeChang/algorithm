# -*- coding: utf-8 -*-
# @Time : 2021/5/17 15:17
# @Author : haojie zhang

from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        nums = [0] * num_people

        sums = 0  # 记录已分发糖果数量
        cnt = 1   # 记录当前要分发的糖果数
        i = 0

        while sums + cnt <= candies:  # 糖果够分发才进行循环
            nums[i % num_people] += cnt
            i += 1
            sums += cnt
            cnt += 1

        nums[i % num_people] += candies - sums  # 将剩余的糖果分给一个人
        return nums


candies = 10
num_people = 3
s = Solution()
print(s.distributeCandies(candies, num_people))




