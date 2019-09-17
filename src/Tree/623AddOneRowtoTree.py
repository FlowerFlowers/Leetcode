'''
leetcode题号：623
给定一个deepth  d  和value  v
在原来树的第d层插入一层，值都是v（如果d-1层有的话）
原来树的d层左子树成为新插入的左儿子的左子树
原来树的d层右子树成为新插入的右儿子的右子树
如果d=1，那么插入根节点，然后原来的根节点是左儿子
eg：
Input:
A binary tree as following:
       4
     /   \
    2     6
   / \   /
  3   1 5

v = 1

d = 2

Output:
       4
      / \
     1   1
    /     \
   2       6
  / \     /
 3   1   5

 Input:
A binary tree as following:
      4
     /
    2
   / \
  3   1

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1
思路：找到第d-1层，然后修改对应的节点即可


'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        else:
            self.goToNextLevel(root,1,d,v)
            return root

    def goToNextLevel(self,node,temp_deepth,d,v):
        #如果还没到达指定深度，那么递归
        if temp_deepth < (d-1) and node:
            left_node = node.left
            right_node = node.right
            temp_deepth +=1
            self.goToNextLevel(left_node,temp_deepth, d,v)
            self.goToNextLevel(right_node,temp_deepth, d,v)
        #如果到达了指定深度
        elif temp_deepth == d-1 and node:
            new_left = TreeNode(v)
            new_right = TreeNode(v)
            new_left.left = node.left
            new_right.right = node.right
            node.left = new_left
            node.right = new_right



