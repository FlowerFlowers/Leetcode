'''
leetcode题号：637
按顺序输出个二叉树每层节点的平均值
eg：
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

思路：深度优先遍历每一个节点，然后一个info记录这层节点的节点数和值的总和作为结果的输出，比如对上面的例子，最终
info = [[3,1],[29,2],[22,2]]
其中info[deepth] = [sum_value,sum_node]
'''
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        info = []
        def dfs(node, deepth):
            if node:
                #如果是该层第一个节点，那么在info中添加一个元素
                if len(info) <= deepth:
                    info.append([0,0])
                info[deepth][0] += node.val
                info[deepth][1] +=1
                #递归的调用本身进行dfs搜索
                dfs(node.left, deepth+1)
                dfs(node.right, deepth+1)
        dfs(root, 0)
        return [value/num for value, num in info]








