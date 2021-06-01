# -*- coding: utf-8 -*-
# @Time : 2021/5/31 17:53
# @Author : haojie zhang


from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board, x, y, word, index):
            if index == len(word)-1:
                return True

            board[x][y] = '#'
            for i, j in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                new_x, new_y = x + i, y + j
                if new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]) \
                        or board[new_x][new_y] != word[index+1]:
                    continue
                if dfs(board, new_x, new_y, word, index+1):
                    return True

            board[x][y] = word[index]
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(board, i, j, word, 0):
                        return True
        return False