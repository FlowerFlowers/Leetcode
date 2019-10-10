'''
leetcode编号：103
按照之字访问二叉树的节点的值
eg：
    3
   / \
  9  20
    /  \
   15   7

output：
[
  [3],
  [20,9],
  [15,7]
]
思路：一个flag位用来判断是从左到右还是从右到左
'''

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        level = [root]
        flag = 1
        while level:
            temp = []
            temp_level = []
            for node in level:
                temp.append(node.val)
                if node.left:
                    temp_level.append(node.left)
                if node.right:
                    temp_level.append(node.right)
            res.append(temp[::flag])
            flag *= (-1)
            level = temp_level
        return res

