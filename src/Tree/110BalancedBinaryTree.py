'''
leetcode题号：110
给定一棵二叉树，看看是不是平衡的
平衡的标准是，叶子节点的高度差不超过1
eg：
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
   Return true.

Example 2:

Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.

思路：
递归的计算每个节点的高度，如果左右儿子的高度差超过1，那么直接结束递归，确定为不平衡
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        self.res = True
        self.getHeight(root)
        return self.res

    def getHeight(self,node):
        #如果res已经是false了，那么之后的判断已经没意义了，尽快结束递归
        if self.res == False:
            return 666
        #递归到到最后就是none，返回0，相当于最底层，if not 判读如果是假，那么执行
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        if abs(left-right)>1:
            self.res = False
        #当前节点的高度相当于左儿子和右儿子最高的+1
        return max(left,right)+1



