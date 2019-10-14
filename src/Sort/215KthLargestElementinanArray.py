'''
leetcode编号：215
找到数组中第k大的数
思路：
堆排序构造大顶堆即可，也可以只维持大小为k的最小堆，如果新的数比最小堆的最小值小就替换，最终最小堆就是最大的k个数，输出最小值即是所需

'''
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def getChild(i):
            return 2*i+1
        #下滤操作，输入堆和i的位置
        def preDown(nums, i):
            temp = nums[i]
            while i < int(len(nums)/2):
                child = getChild(i)
                #找到两个儿子里更大的那个
                if child != len(nums)-1 and nums[child] < nums[child+1]:
                    child += 1
                #如果child的值大于temp，就上移知道找到temp该去的位置
                if nums[child] > temp:
                    nums[i] = nums[child]
                    i = child
                else:
                    break
            nums[i] = temp

        #初始化最大堆，从非叶节点开始下滤：
        for i in range(int(len(nums)/2))[::-1]:
            preDown(nums, i)
        #输出第k大的数
        for j in range(k-1):
            nums[0] = nums[-1]
            nums = nums[:-1]
            preDown(nums, 0)
        return nums[0]


s = Solution()
s.findKthLargest([3, 2, 1, 5, 6, 4],2)
s.findKthLargest([1],1)
s.findKthLargest([-1,2,0],3)