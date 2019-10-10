'''
leetcode70
爬梯子，一次1步或者2步，一共n节，多少种爬法
思路：
斐波那契数列

'''
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return 1
        pre =1
        cur =2
        for i in range(n-2):
            temp = pre+cur
            pre = cur
            cur = temp
        return cur

