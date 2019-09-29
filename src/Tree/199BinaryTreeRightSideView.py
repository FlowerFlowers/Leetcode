'''
leetcode 题号：199
输出从右边看到的树从上到下的值
Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---


思路1：
一个[]存储下一层的每个节点，每次只输出该层最右边节点的值
思路2：
先右子树的dfs，首次到达该深度的时候输出值
'''
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#思路1:
# class Solution:
#     def rightSideView(self, root: TreeNode) -> List[int]:
#         res = []
#         if not root:
#             return res
#         #stack 用来存放之前的节点
#         level = [root]
#         while level:
#             res.append(level[-1].val)
#             next_level = []
#             for leaf in level:
#                 if leaf.left:
#                     next_level.append(leaf.left)
#                 if leaf.right:
#                     next_level.append(leaf.right)
#             level = next_level
#         return res

#思路2：
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        max_deep = 0
        def dfs(node, deep):
            nonlocal max_deep
            if node:
                if deep > max_deep:
                    max_deep = deep
                    res.append(node.val)
                dfs(node.right, deep+1)
                dfs(node.left, deep+1)
        dfs(root, 1)
        return res



