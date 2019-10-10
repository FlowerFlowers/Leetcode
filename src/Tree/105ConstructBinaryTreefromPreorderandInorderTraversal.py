'''
leetcode编号：105
给了一颗树的前序和中序遍历，重建这棵树
For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
思路：
前序遍历依次弹出的可以看成是根节点，在中序遍历里，这个点左边的是左子树，右边的是右子树
'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            value = preorder.pop(0)
            root = TreeNode(value)
            index = inorder.index(value)
            root.left = self.buildTree(preorder,inorder[:index])
            root.right = self.buildTree(preorder,inorder[index+1:])
            return root
