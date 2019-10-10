'''
leetcode编号：173
实现一个类
给定一颗二叉搜索树
要求有两个方法：
1.next（）输出下一个最小的值
2.hasNext()是不是有下一个值
思路：
最简单的想法是先用一个array按顺序存储树的节点即可，但是这样子会浪费额外的空间
我们可以用一个stack存储遍历路上的节点，然后找到最小的，next时候弹出stack中的一个节点，如果这个节点右右子树则加入stack
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._goToLeftest(root)

    def _goToLeftest(self,node):
        while node:
            self.stack.append(node)
            node = node.left


    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        if node.right:
            self._goToLeftest(node.right)
        return node.val


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()