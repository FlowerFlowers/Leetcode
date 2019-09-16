'''
leetcode编号： 251
找到数组中第k大大数
eg：Input: [3,2,1,5,6,4] and k = 2
Output: 5

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

思路：借鉴快速排序，选定一个pivot，大的放一边，小的放一边，确定pivot是list中第几大大数
然后第k大只会出现在一边，相当于只用进行一半的快速排序
一般情况的时间复杂度O(n),最坏情况O(n2)
'''
from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #pos是pivot在list中大位置，nmax代表返回的数是list中第n大大数
        pos = self.partition(nums, 0, len(nums)-1)
        nmax = len(nums)-pos
        if nmax > k:
            return self.findKthLargest(nums[pos+1:], k)
        elif nmax < k:
            return self.findKthLargest(nums[:pos], k-nmax)
        else:
            return nums[pos]

    #以list的右端点array[r]为pivot进行快速排序，返回值是排序后右端点在list中的位置
    def partition(self, array, l, r):
        pivot = array[r]
        i = l-1
        while l < r:
            if array[l] < pivot:
                i +=1
                temp = array[l]
                array[l] = array[i]
                array[i] =temp
            l += 1
        array[i+1], array[r] = array[r], array[i+1]
        return i+1

s=Solution()
print(s.findKthLargest([7,2,4,6,5],3))

