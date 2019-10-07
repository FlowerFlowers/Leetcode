'''
leetcode题号：220
给定一个array，判断是否存在|nums[i]-nums[j]|<=t 并且 i-j<=k
如果存在返回true，否则返回false
思路：
原始的想法是dict[nums[i]]=i,然后判断，但是这样子当t很大的时候效率很低
所以改进的想法是类似于桶排序，每个数字nums[i]放入nums【i】/(t+1)中，那么如果这个桶里已经有数字了，必定返回true
如果这个桶的neighbor出现了数字，判断下两个数字的差值输出
'''
from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        dict = {}
        #w取t+1的原因是|nums[i]-nums[j]|<=t，所以一个桶是t+1个数的集合
        if t < 0:
            return False
        w = t+1
        for i in range(len(nums)):
            #//是除后向下取整
            bucket = nums[i]//w
            #如果有相差<=t的数了，就返回true
            if bucket in dict:
                return True
            if bucket-1 in dict and (nums[i] - dict[bucket-1]) <= t:
                return True
            if bucket+1 in dict and (dict[bucket+1] - nums[i]) <= t:
                return True
            dict[bucket] = nums[i]
            #删除下角标差超过k的记忆
            if i >= k:
                #//是除后向下取整
                del dict[int(nums[i - k] // w)]
        return False

s = Solution()
print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))
print(s.containsNearbyAlmostDuplicate([-3,3], 2, 4))

