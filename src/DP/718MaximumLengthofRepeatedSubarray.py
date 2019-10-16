'''
leetcode编号：718
返回两个数组的最大公共子数组
Input:
A: [1,2,3,2,1]
B: [3,2,1,4,7]
Output: 3
Explanation:
The repeated subarray with maximum length is [3, 2, 1].
思路：
动态规划 dp[i][j]记录以array1[i],array2[j]结束的公共子数组的长度，这时候只有两种情况
1.array1[i]=array2[j]，此时dp[i][j] = dp[i-1][j-1]+1
2.array1[i]不等于array2[j]，此时dp[i][j] =0
初始状态
dp[i][0]=0,dp[0][j]=0
'''
from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        max_len = 0
        for i in range(1,m+1):
            for j in range(1, n+1):
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                    if dp[i][j] > max_len:
                        max_len = dp[i][j]
                else:
                    dp[i][j] = 0
        return max_len

s = Solution()
print(s.findLength([1,2,3,2,1], [3,2,1,4,7]))
