# -*- coding: utf-8 -*-
# @Time : 2021/4/29 11:39
# @Author : haojie zhang

from typing import List

"""
回溯法 在 回溯 前 剪枝 会 大幅降低 运行时间
"""


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def traceback(board, i, j, word, index):
            if index == len(word)-1:
                return True

            board[i][j] = '#'
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                tmp_i = i + x
                tmp_j = j + y
                # 回溯前剪枝
                if tmp_i < 0 or tmp_i >= len(board) or tmp_j < 0 or tmp_j >= len(board[0]) \
                        or board[tmp_i][tmp_j] != word[index+1]:
                    continue
                if traceback(board, tmp_i, tmp_j, word, index + 1):
                    return True
            board[i][j] = word[index]
            return False

        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and traceback(board, i, j, word, 0):
                    return True
        return False


board = [["a"]]
word = "a"
s = Solution()
print(s.exist(board, word))









