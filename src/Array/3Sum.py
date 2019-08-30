'''
leetcode编号：15
eg：
思路：三个都变太混乱了，排序后控制变量，最小的不变，剩下两个一大一小往中间靠拢即可
'''
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #排序
        nums.sort()
        res = []
        #先固定一个
        for i in range(len(nums)-2):
            #从第二次开始判断，如果nums[i]==nums[i-1]说明可能的情况都考虑过了，跳过
            if nums[i]==nums[i-1] and i>0:
                continue
            left = i+1
            right = len(nums)-1
            #如果和是0 添加到结果中
            while left < right:
                s = nums[i]+nums[left]+nums[right]
                if s == 0:
                    res.append((nums[i], nums[left], nums[right]))
                    #如果数列里有重复数字，left和right移动后情况都考虑过了，跳过，
                    #注意一定left < right 写在前面，因为可能出现[0,0,0]会数组越界报错
                    while left < right and nums[left+1] == nums[left]:
                        left += 1
                    while left < right and nums[right-1] == nums[right]:
                        right -= 1
                    #如果匹配，说明left需要增加，right需要减少，才有可能得到下一次匹配
                    left +=1
                    right -=1
                elif s > 0:
                    right -= 1
                else:
                    left += 1
        return res
s = Solution()
list1 = [0,0,0]
print(list1)
print(s.threeSum(list1))