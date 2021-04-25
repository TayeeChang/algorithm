# -*- coding: utf-8 -*-
# @Time : 2021/4/25 10:00
# @Author : haojie zhang

'''
76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：如果 s 中存在这样的子串，我们保证它是唯一的答案。

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
https://leetcode-cn.com/problems/minimum-window-substring/
'''


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        need = defaultdict(int)
        window = defaultdict(int)
        for c in t:
            need[c] += 1
        left, right = 0, 0
        start = 0
        size = float('inf')
        n = len(s)
        valid = 0
        while right < n:
            c = s[right]  # c是要放入窗口的字符
            right += 1  # 右移窗口
            if c in need:  # 进行窗口内一系列数据的更新
                window[c] += 1
                if window[c] == need[c]:
                    valid += 1

            while valid == len(need):  # 缩小窗口
                if right - left < size:  # 缩小之前更新最小覆盖子串结果
                    size = right - left
                    start = left
                c = s[left]   # c 是要移除滑动窗口的字符
                left += 1    # 左移窗口
                if c in need:   # 进行滑动窗口的更新
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1

        return s[start:start+size] if size != float('inf') else ''


s = "ADOBECODEBANC"
t = "ABC"
instance = Solution()
print(instance.minWindow(s, t))