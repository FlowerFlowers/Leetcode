'''
leetcode编号：102
按层输出二叉树的值
eg：
    3
   / \
  9  20
    /  \
   15   7
   output：
   [  [3],  [9,20],  [15,7]]
思路：从根节点开始广度优先遍历即可
'''
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if root is None:
            return res
        queque = [root]
        while queque:
            temp = []
            temp_que = []
            for node in queque:
                temp.append(node.val)
                if node.left:
                    temp_que.append(node.left)
                if node.right:
                    temp_que.append(node.right)
            res.append(temp)
            queque = temp_que
        return res

