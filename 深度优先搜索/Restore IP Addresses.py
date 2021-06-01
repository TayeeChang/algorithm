# -*- coding: utf-8 -*-
# @Time : 2021/5/31 16:18
# @Author : haojie zhang

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def traceback(s, index, dot, tmp):
            if index == len(s) and dot == 4:
                res.append('.'.join(tmp))
                return

            if len(s) - index > (4-dot) * 3:  # 多了---剪枝
                return
            if len(s) - index < (4-dot) * 1:  # 少了--剪枝
                return

            for i in range(index, len(s)):
                if i > index and s[index] == '0':
                    break
                if 0 <= int(s[index:i+1]) <= 255:
                    traceback(s, i+1, dot+1, tmp+[s[index:i+1]])

            return

        res = []
        traceback(s, 0, 0, [])
        return res


s = "010010"
obj = Solution()
print(obj.restoreIpAddresses(s))