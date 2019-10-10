'''
leetcode编号：107
从底到顶，从左到右逐层输出节点顶值
eg：
    3
   / \
  9  20
    /  \
   15   7
output：
[
  [15,7],
  [9,20],
  [3]
]
思路：就是BFS然后最后输出的list反转下就行
'''
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        level = [root]
        while level:
            temp_list = []
            next_level = []
            for node in level:
                temp_list.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            res.append(temp_list)
            level = next_level
        return res[::-1]


