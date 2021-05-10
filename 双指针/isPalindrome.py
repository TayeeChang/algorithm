# -*- coding: utf-8 -*-
# @Time : 2021/5/10 15:35
# @Author : haojie zhang


class Solution:
    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s)-1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        return True


s = "0P"
obj = Solution()
print(obj.isPalindrome(s))