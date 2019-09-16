'''
leetcode题号   903
给一个序列由'I'（递增）和'D'（递减）组成
比如'DID'，那么就用1，2，3，4组合满足减增减的有几个情况
eg：
Input: "DID"
Output: 5
Explanation:
The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)

思路：动态规划
见onenote
'''
class Solution:
    def numPermsDISequence(self, S: str) -> int:
        dp = [1]*(len(S)+1)
        for i in range(len(S)):
            if S[i] == 'D':
                dp =dp[1:]
                for j in range(len(dp)-1)[::-1]:
                    dp[j] +=dp[j+1]
            elif S[i] == 'I':
                dp =dp[:-1]
                for j in range(1,len(dp)):
                    dp[j] += dp[j-1]
        return dp[0] % (10**9+7)

