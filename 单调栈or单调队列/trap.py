# -*- coding: utf-8 -*-
# @Time : 2021/4/22 15:20
# @Author : haojie zhang

# 接雨水


# 单调栈or单调队列

def trap(height):
    stack = []
    res = 0
    for i in range(len(height)):
        while stack and height[stack[-1]] <= height[i]:
            h = height[stack[-1]]
            stack.pop()
            if stack:
                width = i - stack[-1] - 1
                res += width * (min(height[i], height[stack[-1]]) - h)
        stack.append(i)
    return res


# 双指针
def trap_2_points(height):
    if not height:
        return 0
    left, right = 0, len(height)-1
    l_max, r_max = 0, 0
    res = 0
    while left <= right:
        if l_max < r_max:
            l_max = max(l_max, height[left])
            res += l_max - height[left]
            left += 1
        else:
            r_max = max(r_max, height[right])
            res += r_max - height[right]
            right -= 1
    return res


height = [4, 2, 0, 3, 2, 5]
print(trap(height))