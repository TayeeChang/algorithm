# -*- coding: utf-8 -*-
# @Time : 2021/5/4 15:10
# @Author : haojie zhang


from typing import List

"""
1079. 活字印刷
你有一套活字字模 tiles，其中每个字模上都刻有一个字母 tiles[i]。返回你可以印出的非空字母序列的数目。

注意：本题中，每个活字字模只能使用一次。


示例 1：

输入："AAB"
输出：8
解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。
示例 2：

输入："AAABBC"
输出：188
"""


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        # 本质是排列问题
        def dfs(tiles, tmp):
            if tmp:
                nonlocal res
                res += 1

            for i in range(len(tiles)):
                if i > 0 and tiles[i] == tiles[i - 1]:
                    continue
                dfs(tiles[:i] + tiles[i + 1:], tmp + tiles[i])

        res = 0
        tiles = ''.join(sorted(list(tiles)))
        dfs(tiles, '')
        return res