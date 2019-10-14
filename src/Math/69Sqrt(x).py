'''
leetcode 编号：69
求一个数的平方根，结果保留整数
思路：满足n2<x2<(n+1)2的就是结果，然后二分查找提高效率
'''
#结果保留整数
# class Solution:
#     def mySqrt(self, x: int) -> int:
#         down, up = 0, x
#         while down <= up:
#             mid = (down + up) // 2
#             if mid*mid <= x < (mid+1)*(mid+1):
#                 return mid
#             elif mid*mid > x:
#                 up = mid-1
#             else:
#                 down = mid+1

#结果保留小数点后一位
class Solution:
    def mySqrt(self, x: int) -> int:
        down, up = 0, x
        mid = (down + up) / 2
        while abs(mid*mid-x) > 0.05:
            if mid*mid < x:
                down = mid
            else:
                up = mid
            mid = (down + up) / 2
        return round(mid,1)
s = Solution()
print(s.mySqrt(8))