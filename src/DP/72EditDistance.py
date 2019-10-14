'''
leetcode编号：72
求两个字符串的编辑距离
只能进行以下操作：
1.插入
2.删除
3.替换
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')


思路：动态规划dp[len_a][len_b]储存字符串a长为len_a变成字符串b长为len_b时候的编辑距离
假如我们想知道str1a是如何变成str2b的有三种路径可以完成这个事情
1. 替换：已知str1->str2，那么只需要给str1增加a，str2增加b即可，这相当于一步替换，如果a，b相同，那么就不用操作
所以此时dp[i][j] = dp[i-1][j-1](a==b) or dp[i-1][j-1]+1(a is not b)
2. 插入：已知str1a->str2，那么只需要在这个基础上再插入b即可，此时dp[i][j] = dp[i][j-1]+1
3.删除: 已知str1 -> str2b,那么str1a->str2b只需要在这个基础上把多的'a'删除即可 此时dp[i][j] = dp[i-1][j]+1
真实的情况自然是三种变换路径选择最短的走即可，最终dp[len(str1)][len(str2)]即为答案

初始条件dp[0][j] = j(全部插入操作)，dp[i][0] = i （全部删除操作）
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[float('inf') for i in range(n+1)] for j in range(m+1)]
        #初始化
        for i in range(m+1):
            dp[i][0] = i
        for j in range(n+1):
            dp[0][j] = j
        #动态规划
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    replace_dp = dp[i-1][j-1]
                else:
                    replace_dp = dp[i-1][j-1]+1
                insert_dp = dp[i][j-1]+1
                delet_dp = dp[i-1][j] + 1
                dp[i][j] = min(replace_dp, insert_dp, delet_dp)
        return dp[m][n]

s = Solution()
print(s.minDistance('horse', 'ros'))
print(s.minDistance('intention', 'execution'))


