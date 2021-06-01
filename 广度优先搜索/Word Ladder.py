# -*- coding: utf-8 -*-
# @Time : 2021/5/29 16:03
# @Author : haojie zhang

from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        from collections import deque
        if not wordList:
            return 0
        if endWord not in wordList:
            return 0

        wordset = set(wordList)
        visited = set([beginWord])

        queue = deque()
        queue.append((beginWord, 1))
        while queue:
            word, level = queue.popleft()
            if word == endWord:
                return level

            for i in range(len(word)):
                for j in range(26):
                    new_word = word[:i] + chr(ord('a')+j) + word[i+1:]
                    if new_word in wordset and new_word not in visited:
                        visited.add(new_word)
                        queue.append((new_word, level+1))
        return 0


