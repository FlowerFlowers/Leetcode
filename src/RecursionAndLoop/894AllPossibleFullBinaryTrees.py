'''
leetcode编号 ：894
给n个节点构成二叉树，要求每个节点要么有两个儿子，要么没有儿子,节点的值均为1，求所有可能的树
思路：
递归
如果只有根节点，那么就一种可能
如果有3个节点，那么也1种可能
如果有5个节点，除去根节点，可以分为左1右3或者左3右1两种情况，左右分别返回子树给根节点，这都是之前解决过的
所以：
初始情况是只有一个节点，然后其他情况都递归到这种情况
'''


# Definition for a binary tree node.
from  typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        res = []
        if N % 2 == 0:
            return res
        if N == 0:
            return res
        root = TreeNode(0)
        if N == 1:
            return [root]
        N = N-1
        for i in range(1, N, 2):
            left_res = self.allPossibleFBT(i)
            right_res = self.allPossibleFBT(N-i)
            for left in left_res:
                for right in right_res:
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    res += [root]
        return res



