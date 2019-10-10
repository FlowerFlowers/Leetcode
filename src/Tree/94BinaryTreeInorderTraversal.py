'''
leetcode题号：94
二叉树的中序遍历
Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

思路：
递归实现：先递归调用左儿子，然后添加自己的值，然后调用右儿子

迭代实现：用一个stack，沿着左子树遍历，节点先依次存在栈里，然后每弹出一个节点，就访问它的右子树
'''
# Definition for a binary tree node.

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
递归实现
'''
# class Solution:
#     def inorderTraversal(self, root: TreeNode) -> List[int]:
#         res = []
#         self.helper(root, res)
#         return res
#
#     def helper(self,node,res):
#         if node:
#             self.helper(node.left, res)
#             res.append(node.val)
#             self.helper(node.right, res)



'''
迭代实现：

'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack =[]
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            #注意：stack是否为空的判断必须放在这里，如果放到后面，那么根节点的左子树遍历完就会输出
            if stack == []:
                return res
            node = stack.pop()
            res.append(node.val)
            node = node.right

