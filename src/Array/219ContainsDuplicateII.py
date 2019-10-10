'''
leetcode编号：219
给一个数组，判断是不是有重复元素，并且重复元素之间的距离小于等于k，如果有就返回true，如果没有就返回false
Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

思路：一个dict  key是值，value是上一次看到这个值的位置，判断即可
'''
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict = {}
        for i in range(len(nums)):
            #不是第一次出现
            if nums[i] in dict:
                if i - dict[nums[i]] <= k:
                    return True
                dict[nums[i]] = i
            #第一次出现
            else:
                dict[nums[i]] = i
        return False
