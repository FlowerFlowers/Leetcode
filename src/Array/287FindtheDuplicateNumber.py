'''
leetcode编号：287
给定一个array，共n+1个数字，每个数字都介于1-n之间，找出那个重复出现都数字（只有一个数字重复出现，但是可以重复出现多次）
要求：
不能改变数组，空间复杂度O（1），时间复杂度最大O（n2）
Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
思路1：
二分的想法，统计1-n/2出现的个数，如果多于2/n，那么就代表重复数字在这边，依次类推，时间复杂度O（nlogn）
思路2：
链表成环，nums看成一个链表   index----value
eg：nums=[1,3,4,2,2]
相当于链表是0---1----3---2----4----2（从2-2成环了）
然后一个runner，一个walker开始走，相遇代表成环
然后一个walker1从nums【0】开始走，一个walker2从相遇点开始走，相遇的时候就是重复数字，也就是环的入口
空间复杂度O(1)   时间复杂度O（n）
'''
#思路1
# from typing import List
# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int:
#         low = 0
#         high = len(nums)
#         while high - low > 1:
#             count = 0
#             mid = (high+low)//2
#             for k in nums:
#                 if low < k <= mid:
#                     count += 1
#             if count <= mid-low:
#                 low = mid
#             else:
#                 high = mid
#         return high



#思路2
class Solution:
    def findDuplicate(self, nums):
        runner = nums[0]
        walker = nums[0]
        while True:
            #让快慢两个节点相遇
            runner = nums[nums[runner]]
            walker = nums[walker]
            if runner == walker:
                break
        walker1 = nums[0]
        walker2 = runner
        while walker1 != walker2:
            walker1 = nums[walker1]
            walker2 = nums[walker2]
        return walker1
s = Solution()
res = s.findDuplicate([1, 4, 4, 2, 4])
print(res)

