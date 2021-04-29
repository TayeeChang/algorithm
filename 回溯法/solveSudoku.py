# -*- coding: utf-8 -*-
# @Time : 2021/4/29 10:23
# @Author : haojie zhang

from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def traceback(board, i, j):
            if i == 9:
                return True
            if j == 9:
                return traceback(board, i+1, 0)

            for k in range(1, 10):
                if board[i][j] != '.':
                    return traceback(board, i, j+1)
                if not isvalid(board, i, j, str(k)):
                    continue
                board[i][j] = str(k)
                if traceback(board, i, j+1):
                    return True
                board[i][j] = '.'
            return False

        def isvalid(board, r, c, ch):
            for i in range(9):
                if board[r][i] == ch:
                    return False
                if board[i][c] == ch:
                    return False
                # if board[r//3*3 + i//3][c//3*3 + i%3] == ch: # 这种写法是错误的
                if board[r // 3 * 3 + i // 3][c // 3 * 3 + i % 3] == ch:
                    return False
            return True

        traceback(board, 0, 0)


board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

s = Solution()
s.solveSudoku(board)
print(board)












