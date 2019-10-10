'''
leetcode编号：217
找到list是不是有重复元素
思路：建立dict，第一次遇到元素添加key，第二次遇到输出true
'''
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                return True
            else:
                dict[nums[i]] =1
        return False
