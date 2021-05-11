# -*- coding: utf-8 -*-
# @Time : 2021/5/11 17:27
# @Author : haojie zhang


def numberOfContinuousAlphas(s):
    res = 1
    cnt = 1
    ch = s[0]
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            cnt += 1
            if cnt > res:
                ch = s[i]
                res = cnt
        else:
            cnt = 1
    return res, ch


s = 'aaaabbaacccccdde'
print(numberOfContinuousAlphas(s))