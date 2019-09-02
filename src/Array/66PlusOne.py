'''
leetcode题号：66
给一个用list存储的数，加一后输出
eg：[1,2,3]->[1,2,4]     [4,3,2,1]->[4,3,2,2]
思路：
从最后一位开始看，不是9就+1，是9就这一位变成0后，递归给前一位，直到不是9
如果都是9，那么最前面+1
'''
class Solution:
    #使用类时需要self作为第一个参数，指类的实例本身
    def plusOne(self, digits):
        #使用递归算法
        #如果出现999的情况
        if (len(digits)==0):
            digits=[1]
        #如果最后一位是9，那么这一位归0，任务递归的交给上一位
        elif (digits[-1]==9):
            digits = self.plusOne(digits[:-1])
            digits.extend([0])
        #第一次遇到不是9的位，+1即可
        else:
            digits[-1] +=1
        return digits
s = Solution()
print(s.plusOne([1,2,3,4]))
print(s.plusOne([1,2,9,9]))
print(s.plusOne([9,9,9,9]))

