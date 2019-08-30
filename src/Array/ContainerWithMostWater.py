'''
leetcode题号：11
给定一个array，每个数字代表对应位置有相应高度的柱子，然后选择两个位置和x轴构成的矩形面积最大
eg:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
解释：从第一个8---最后一个7，矩形的长是7，高也是7，所以面积是49
思路：
如果a[0]<a[5],那么 (0, 4), (0, 3), (0, 2), (0, 1) 的面积都会小于 (0, 5)，
因为矩形的高不会超过a[0],长又比（0，5）短
所以可以从最左和最右开始，每次选择一边缩进，直到矩形的长为0
'''
from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, width, area = 0, len(height)-1, len(height)-1, 0
        while width > 0:
            #计算面积
            area = max(area,width*min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            width -= 1
        return area

