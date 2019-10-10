'''
leetcode编号：240
一个二维数组，每一行从左到右是递增的，每一列从上到下是递增的，判断是不是存在一个target
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.


思路1：
从第一列开始，如果数在这一列的范围内就扫，不在就不扫,时间复杂度O（n2）
思路2：
从右上角（或者左下角）开始
比如从右上角开始，如果这个数字小于target，那么这行排除，如果这个数字大于target，那么这列排除

'''
#思路1
# class Solution:
#     def searchMatrix(self, matrix, target):
#         '''
#         :type matrix: List[List[int]]
#         :type target: int
#         :rtype: bool
#         '''
#         if matrix == [] or matrix ==[[]] or target is None:
#             return False
#         rows, cols = len(matrix), len(matrix[0])
#         for col in range(cols):
#             if matrix[0][col] == target:
#                 return True
#             if matrix[rows-1][col] == target:
#                 return True
#             if matrix[0][col] < target < matrix[rows-1][col]:
#                 for row in range(rows):
#                     if matrix[row][col] == target:
#                         return True
#         return False


#思路2：
class Solution:
    def searchMatrix(self, matrix, target):
        '''
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        '''
        if matrix == [[]] or matrix == [] or target is None:
            return False
        row_index, col_index, sum_row = 0, len(matrix[0])-1, len(matrix)
        while row_index < sum_row and col_index >= 0:
            if matrix[row_index][col_index] == target:
                return True
            elif matrix[row_index][col_index] > target:
                col_index -= 1
            else:
                row_index += 1
        return False

s = Solution()
res = s.searchMatrix([
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
],5)
print(res)