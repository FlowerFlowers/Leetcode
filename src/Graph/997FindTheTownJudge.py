'''
leetcode题号99
一个小镇有N个人，可能有1个法官或没有，要求：
1.法官不信任任何人
2.其他人都信任法官
如果有法官，请找出法官，没有返回-1
Example 1:

Input: N = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: N = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: N = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: N = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: N = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3

思路：法官需要入度为N-1，出度为0，又因为题目限制一个人不能信任自己，那么算入-出=N-1即为答案
'''
from typing import List


class Solution:

    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        #为了方便直接对应编号，count[0]无意义
        count = [0]*(N+1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1, len(count)):
            if count[i] == N-1:
                return i
        return -1
