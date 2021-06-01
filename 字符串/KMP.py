# -*- coding: utf-8 -*-
# @Time : 2021/5/19 9:42
# @Author : haojie zhang


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getNext(t):
            k, j = -1, 0
            nextN = [-1] * len(t)
            while j < len(t)-1:
                if k == -1 or t[k] == t[j]:
                    k += 1
                    j += 1
                    if j < len(t) and t[k] != t[j]:  #
                        nextN[j] = k
                    else:
                        nextN[j] = nextN[k]
                else:
                    k = nextN[k]
            return nextN

        def KMP(s, t):
            nextN = getNext(t)
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if j == -1 or s[i] == t[j]:
                    i += 1
                    j += 1
                else:
                    j = nextN[j]
            if j == len(t):
                return i - j
            return -1

        return KMP(haystack, needle)


s = 'aaaabfff'
t = 'aabaabaaf'
obj = Solution()
print(obj.strStr(s, t))