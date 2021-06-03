# -*- coding: utf-8 -*-
# @Time : 2021/6/2 15:05
# @Author : haojie zhang

from typing import List
# 自顶向下的递归

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hashMap = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'
                   }

        def dfs(digits, index):
            if index == len(digits):
                return ['']
            res = []
            if index < len(digits):
                ch = digits[index]
                s = hashMap[ch]
                tmp = dfs(digits, index+1)
                res += [v + t for v in s for t in tmp]
            return res

        if not digits:
            return []

        return dfs(digits, 0)

# 自底向上的递归

class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        hashMap = {'2': 'abc',
                   '3': 'def',
                   '4': 'ghi',
                   '5': 'jkl',
                   '6': 'mno',
                   '7': 'pqrs',
                   '8': 'tuv',
                   '9': 'wxyz'
                   }

        def dfs(digits, index, tmp):
            if index == len(digits):
                res.append(tmp)
                return
            for ch in hashMap[digits[index]]:
                dfs(digits, index+1, tmp+ch)

        if not digits:
            return []
        res = []
        dfs(digits, 0, '')
        return res


digits = '23'
s = Solution()
print(s.letterCombinations(digits))