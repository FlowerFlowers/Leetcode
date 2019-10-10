'''
leetcode编号：144
先序遍历树
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]

思路：
递归：先输出自己的val，然后递归调用左儿子，然后递归调用右儿子
迭代：使用stack，每次弹出一个node，然后node的值加入res，右儿子，左儿子依次入栈
'''
# Definition for a binary tree node.
from typing import  List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         self.helper(root, res)
#         return res
#
#     def helper(self, node, res):
#         if node:
#             res.append(node.val)
#             self.helper(node.left, res)
#             self.helper(node.right, res)

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        while stack:
            temp_node = stack.pop()
            #因为可能有none入栈，所以需要检验
            if temp_node:
                res.append(temp_node.val)
                stack.append(temp_node.right)
                stack.append(temp_node.left)
        return res

