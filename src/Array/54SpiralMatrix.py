from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if matrix == [] or matrix == [[]]:
            return []
        else:
            m, n = len(matrix), len(matrix[0])
            res = []
            left, up, right, down = 0, 0, n, m
            flag = 'left_to_right'
            while up < down and left < right:
                if flag == 'left_to_right':
                    for i in range(left, right):
                        res.append(matrix[up][i])
                    up += 1
                    flag = 'up_to_down'
                elif flag == 'up_to_down':
                    for i in range(up, down):
                        res.append(matrix[i][right - 1])
                    right -= 1
                    flag = 'right_to_left'
                elif flag == 'right_to_left':
                    for i in range(left, right)[::-1]:
                        res.append(matrix[down - 1][i])
                    down -= 1
                    flag = 'down_to_up'
                elif flag == 'down_to_up':
                    for i in range(up, down)[::-1]:
                        res.append(matrix[i][left])
                    left += 1
                    flag = 'left_to_right'
        return res

s = Solution()
print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(s.spiralOrder([]))

