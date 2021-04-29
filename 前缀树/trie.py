# -*- coding: utf-8 -*-
# @Time : 2021/4/29 14:38
# @Author : haojie zhang

import collections


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            node = node.setdefault(char,{})

        node["end"] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]

        return "end" in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]

        return True



word1 = 'apple'
word2 = 'google'
prefix = 'app'
obj = Trie()
obj.insert(word1)
obj.insert(word2)
param_2 = obj.search(word1)
param_3 = obj.startsWith(prefix)

