'''
leetcode 题号：1042
一张图，N个节点，每个节点的度不超过3，用1，2，3，4四种颜色染色
相邻节点不同色
给出一种解决方案
Example 1:

Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Example 2:

Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
思路：
贪心即可，因为每个节点的度不超过3，不回存在没法染色的情况
'''
from typing import List
class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        graph = [[] for i in range(N)]
        res = [0]*N
        #生成图
        for i , j in paths:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)
        #计算每个节点邻近节点的颜色，选一个没用过的
        for i in range(len(graph)):
            adj_cor = set()
            for adj in graph[i]:
                if res[adj] != 0:
                    adj_cor.add(res[adj])
            res[i] = ({1,2,3,4}-adj_cor).pop()
        return  res



