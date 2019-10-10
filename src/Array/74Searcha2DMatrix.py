'''
leetcode 编号74
一个二维数组，每一行从左到右递增
下一列的第一个比上一列的最后一个大
判断是否存在某个target
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
思路1：
先按照列走，找到matrix[i][0]<target<<matrix[i+1][0],然后按照行找
思路2：
看成一维数组，进行二分查找

'''
from typing import List

#思路1
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         if matrix == [[]] or matrix == []:
#             return False
#         m, n = len(matrix), len(matrix[0])
#         tar_row = m-1
#         for i in range(m):
#             if matrix[i][0] > target:
#                 tar_row = i-1
#                 break
#             if matrix[i][0] == target:
#                 return True
#         for j in range(n):
#             if matrix[tar_row][j] == target:
#                 return True
#         return False

#思路2：
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [[]] or matrix == [] or target is None:
            return False
        row, col = len(matrix), len(matrix[0])
        low, upper = 0, row*col
        while low != upper:
            mid = (low+upper)//2
            print(mid)
            row_index, col_index = (mid//col), mid % col
            print(matrix[row_index][col_index])
            if matrix[row_index][col_index] == target:
                return True
            if matrix[row_index][col_index] < target:
                low = mid+1
            else:
                upper = mid
        return False

s = Solution()
print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))


