'''
leetcode题号：18
给定一个list，输出所有可能的情况，用list中的四个数相加和数target
eg：
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
思路：我们只会两个数相加，那么对于三个数相加可以先固定一个数，变成两个数相加。四个数变成三个数，递归
'''
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def Nsum(nums,target,N,pre_result):
            if len(nums) < N or N < 2:
                return
            #计算初始N=2的情况
            if N == 2:
                left = 0
                right = len(nums)-1
                results = []
                while left < right:
                    if nums[left] + nums[right] == target:
                        results.append(pre_result+[nums[left], nums[right]])
                        left +=1
                        right -=1
                        #如果有重复元素，继续往前走，因为结果重复
                        while nums[left] == nums[left-1] and left < right:
                            left += 1
                        while nums[right] == nums[right+1] and left < right:
                            right -=1
                    elif nums[left] + nums[right] < target:
                        left +=1
                    elif nums[left] + nums[right] > target:
                        right -=1
                return results
            #多于两个元素
            else:
                results = []
                for i in range(len(nums)-N+1):
                    #防止重复
                    if i == 0 or (i>0 and nums[i] != nums[i-1]):
                        temp_results = Nsum(nums[i+1:], target-nums[i], N-1, pre_result+[nums[i]])
                        results += temp_results
                return results

        fin_results = Nsum(sorted(nums), target, 4, [])
        return fin_results
s = Solution()
print(s.fourSum([0,0,0,0],0))


