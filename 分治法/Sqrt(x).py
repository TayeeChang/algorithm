# -*- coding: utf-8 -*-
# @Time : 2021/6/1 10:47
# @Author : haojie zhang

class Solution2:
    def mySqrt(self, x: int) -> int:
        lift,right = 0,x
        while(lift<=right):
            mid = (lift+right)//2
            if mid**2<=x:
                lift=mid+1
            if mid**2>x:
                right=mid-1

        return right


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        lo, hi = 0, x // 2 + 1
        while lo < hi:
            mid = lo + (hi-lo) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1


# class Solution1:
#     def mySqrt(self, x: int, epsilon: float) -> int:
#
#         lo, hi = 0, x / 2 + 1
#         while lo < hi:
#             mid = lo + (hi-lo) / 2
#             if abs(mid * mid - x) <= epsilon:
#                 return mid
#             elif mid * mid < x:
#                 lo = mid
#             else:
#                 hi = mid
#         return lo

x = 2
s = Solution()
print(s.mySqrt(x))

