'''
leetcode 题号：217
给定一个数组，判断有没有重复数字
有重复数组就返回true 否则返回false
Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
思路1：
构建一个字典，第二次访问到某个数字就返回true
时间复杂度O（n） 空间复杂度O（n）
思路2：判断数组nums的长度和集合nums的长度是不是一致

'''
from typing import List
#思路1
# from collections import defaultdict
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         dict = defaultdict(lambda: 0)
#         for i in range(len(nums)):
#             dict[nums[i]] += 1
#             if dict[nums[i]] > 1:
#                 return True
#         return False

#思路2：
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))
