# -*- coding: utf-8 -*-
# @Time : 2021/4/24 13:21
# @Author : haojie zhang


def trap_2_points(height):
    if not height:
        return 0
    left, right = 0, len(height)-1
    l_max, r_max = height[0], height[-1]
    res = 0
    while left <= right:
        l_max = max(l_max, height[left])
        r_max = max(r_max, height[right])
        if l_max < r_max:
            res += l_max - height[left]
            left += 1
        else:
            res += r_max - height[right]
            right -= 1
    return res


height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap_2_points(height))