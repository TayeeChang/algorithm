# -*- coding: utf-8 -*-
# @Time : 2021/4/29 15:45
# @Author : haojie zhang

from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        WORD_KEY = '$'
        for word in words:
            node = trie
            for ch in word:
                node = node.setdefault(ch, {})
            node[WORD_KEY] = word

        matchedWords = []

        def traceback(board, i, j, trie):

            ch = board[i][j]
            currNode = trie[ch]

            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                matchedWords.append(word_match)

            board[i][j] = '#'
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                tmp_i = i + x
                tmp_j = j + y
                if tmp_i < 0 or tmp_i >= len(board) or tmp_j < 0 or tmp_j >= len(board[0]):
                    continue
                if board[tmp_i][tmp_j] not in currNode:
                    continue
                traceback(board, tmp_i, tmp_j, currNode)

            board[i][j] = ch
            if not currNode:
                trie.pop(ch)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    traceback(board, i, j, trie)
        return matchedWords


board = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]]
words = ["oa","oaa"]
s = Solution()
print(s.findWords(board, words
                  ))

