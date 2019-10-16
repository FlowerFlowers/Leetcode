'''
leetcode编号：1143
寻找两个字符串的最长公共子序列
Example 1:

Input: text1 = "abcde", text2 = "ace"
Output: 3
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.
Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

思路：动态规划
dp[i][j]表示str1[:i+1]和str2[:j+1]的最长公共子序列的长度
那么可以考虑如下情况str1a和str2b
1.a=b，那么这时候相当于之前的公共子序列+1 即dp[i][j] = dp[i-1][j-1]+1
2.a不等于b，那么这时候dp[i][j] = max(dp[i-1][j],dp[i][j-1])

'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dp = [[0 for i in range(n2+1)] for j in range(n1+1)]
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        return dp[-1][-1]


s = Solution()
print(s.longestCommonSubsequence('abcde', 'ace'))
print(s.longestCommonSubsequence('abc', 'abc'))
print(s.longestCommonSubsequence('abc', 'def'))




