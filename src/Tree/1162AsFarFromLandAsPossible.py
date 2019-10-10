'''
leetcode编号：1162
一个n*n的矩阵，1代表陆地，0代表水，采用曼哈顿距离
求出距离陆地最远的水的距离

Example 1:
Input: [[1,0,1],[0,0,0],[1,0,1]]
Output: 2
Explanation:
The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:
Input: [[1,0,0],[0,0,0],[0,0,0]]
Output: 4
Explanation:
The cell (2, 2) is as far as possible from all the land with distance 4.

思路：
先找到所有陆地的位置，用stack存放，然后把距离1的格子染色，然后这些被染色的格子继续把距离1的格子染色，直到全部完成染色

'''
from typing import List
class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        #寻找出来所有陆地
        stack = [[i,j] for i in range(n) for j in range(n) if grid[i][j] == 1]
        #如果都是陆地或者都是水
        if len(stack) == 0 or len(stack) == n*n:
            return -1
        level = 0
        while stack:
            size = len(stack)
            for _ in range(size):
                x0, y0 = stack.pop(0)
                for i,j in [(-1, 0), (1, 0), (0, 1), (0, -1)] :
                    #如果没出格,并且原来是水
                    if 0 <= x0+i < n and 0 <= y0+j < n and grid[x0+i][y0+j]==0:
                        stack.append([x0+i, y0+j])
                        grid[x0+i][y0+j] = 1
            level += 1
        #-1是因为最后一片水变陆地时候+1了，这个+1是没意义的
        return level-1


s = Solution()
a = s.maxDistance([[1,0,1],[0,0,0],[1,0,1]])
print(a)



