'''
合并两个排列好的数组
思路：从长数组的尾部开始更新，保证无风险
'''
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # while 使m,n同时开始循环，m代表nums1有效数字个个数，n代表nums2有效数字个数
        #从尾到头的顺序保证了替换过程的无风险
        while m > 0 and n > 0:
            if (nums1[m - 1] > nums2[n - 1]):
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        print(nums1)


s = Solution()
s.merge([1,2,3,0,0,0],3,[2,5,6],3)
s.merge([-1,0,0,3,3,3,0,0,0],6,[1,2,2],3)

