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

'''
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = [[0 for i in range(2)] for j in range(len(nums))]
        if len(nums) == 0:
            return 0
        res[0][0] = 1
        res[0][1] = nums[0]
        temp_max = 1
        for i in range(1, len(nums)):
            for j in range(i)[::-1]:
                if res[j][1] < nums[i] and res[j][0] >= res[i][0]:
                    res[i][0] = res[j][0]+1
                    res[i][1] = nums[i]
                    if temp_max < res[i][0]:
                        temp_max = res[i][0]
            if res[i][0] == 0:
                res[i][0] = 1
                res[i][1] = nums[i]
            print(res)
        return temp_max

s = Solution()
s.lengthOfLIS([1,3,6,7,9,4,10,5,6])