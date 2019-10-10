'''
leetcode编号：300
确定最大递增子序列的最大长度：
Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
思路1：
动态规划
res[i][length，max_num]用来存储以目前位置为结束的最大长度和最大值
计算的时候看之前的max_num小于当前值的最大长度+1，即为当前位置结尾的最大长度
思路2：
动态规划
我们从左往右一个一个增加数字，然后用tail[i]记录长度为i+1的子序列的最小末尾值，length记录最长子序列的长度
这时候有两种情况：
1.新加入的数比之前tail[-1]还要大，那么可以加在递增子序列的最后一个，length+1
2.新加入的数介于tail[i]和tail[i+1]之间，那么这时候tail[i]=新加入的数，相当于保证固定长的子序列，可以用更小的数结束了
因为tail一定是递增的，所以对于新的数插入的位置可以二分查找，这样子复杂度logn，一共插入n次，那么总的复杂度只有nlogn
'''
from typing import List

#思路1：动态规划
# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         res = [[0 for i in range(2)] for j in range(len(nums))]
#         if len(nums) == 0:
#             return 0
#         res[0][0] = 1
#         res[0][1] = nums[0]
#         temp_max = 1
#         for i in range(1, len(nums)):
#             for j in range(i)[::-1]:
#                 if res[j][1] < nums[i] and res[j][0] >= res[i][0]:
#                     res[i][0] = res[j][0]+1
#                     res[i][1] = nums[i]
#                     if temp_max < res[i][0]:
#                         temp_max = res[i][0]
#             if res[i][0] == 0:
#                 res[i][0] = 1
#                 res[i][1] = nums[i]
#             print(res)
#         return temp_max


#思路2：
class Solution:
    def lengthOfLIS(self, nums):
        tail = [float('inf')]*len(nums)
        if not nums:
            return 0
        size = 0
        for num in nums:
            #i,j用来记录二分查找的指针
            i, j = 0, size
            while i !=j:
                m = int((i+j)/2)
                if tail[m] < num:
                    i = m+1
                else:
                    j = m
            #更新tail
            tail[i] = num
            #如果是在最后加了一个数，那么size+1
            size = max(size, i+1)
        return size



s = Solution()
print(s.lengthOfLIS([10,9,2,5,3,7,101,18]))
#print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6,8,11]))
