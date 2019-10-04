'''
leetcode编号：98
判断一颗二叉树是不是二叉搜索树（对任何一个节点，左子树的值都小于当前节点的值，右子树的值都大于当前节点的值）
eg：
    2
   / \
  1   3

Input: [2,1,3]
Output: true


    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
思路：
递归的过程中传递当前节点值限制的范围lower--upper
然后左子树限制的范围就变成了lower--node.val
右子树限制的范围就变成了node.val---upper
初始条件根节点限制的范围是-inf---inf

每个节点检测是不是在要求的边界内，以及左右子树是不是满足条件
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        #float('inf')正无穷
        return self.helper(root, -float('inf'), float('inf'))

    def helper(self, node, lower_bound, upper_bound):
        if not node:
            return True
        if node.val >= upper_bound:
            return False
        if node.val <= lower_bound:
            return False
        left = self.helper(node.left, lower_bound, node.val)
        right = self.helper(node.right, node.val, upper_bound)
        return left and right


