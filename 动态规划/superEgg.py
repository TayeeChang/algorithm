# -*- coding: utf-8 -*-
# @Time : 2021/4/23 23:35
# @Author : haojie zhang

# 基础版 时间复杂度（O(kn^2)）肯定超时


def superEggDrop(k: int, n: int) -> int:
    if k == 1:
        return n
    if n == 0:
        return 0
    if (k, n) in memo:
        return memo[(k, n)]
    res = float('inf')
    for i in range(1, n+1):
        res = min(res,
                  max(superEggDrop(k-1, i-1),
                      superEggDrop(k, n - i)) + 1
                  )
    memo[(k, n)] = res
    return res


def superEggDrop1(k: int, n: int) -> int:
    if k == 1:
        return n
    if n == 0:
        return 0
    if (k, n) in memo:
        return memo[(k, n)]

    res = float('inf')
    low, high = 1, n
    while low <= high:
        mid = low + (high - low) // 2
        broken = superEggDrop1(k-1, mid-1) + 1
        un_broken = superEggDrop1(k, n-mid) + 1
        if broken < un_broken:
            low = mid + 1
            res = min(res, un_broken)
        elif broken > un_broken:
            high = mid - 1
            res = min(res, broken)
        else:
            res = min(res, broken)
            break
    memo[(k, n)] = res
    return res


memo = {}
print(superEggDrop1(2, 2))